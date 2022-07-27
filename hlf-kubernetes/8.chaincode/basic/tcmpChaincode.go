/*
SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/golang/protobuf/ptypes"
	"github.com/hyperledger/fabric-chaincode-go/shim"
	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type serverConfig struct {
	CCID    string
	Address string
}

// SmartContract provides functions for managing an asset
type SmartContract struct {
	contractapi.Contract
}

// Asset describes basic details of what makes up a simple asset
type AccountOrderLog struct {
	ID         string `json:"id"`
	OrderID    string `json:"orderID"`
	PrevStatus string `json:"prevStatus"`
	Status     string `json:"status"`
	Comment    string `json:"comment"`
	ReviewerID string `json:"reviewerID"`
	CreateTime string `json:"createTime"`
	UpdateTime string `json:"updateTime"`
	CreateBy   string `json:"createBy"`
	UpdateBy   string `json:"updateBy"`
	// Features   string `json:"feature,omitempty"`
}

// HistoryQueryResult structure used for returning result of history query
type HistoryQueryResult struct {
	Record    *AccountOrderLog `json:"record"`
	TxId      string           `json:"txId"`
	Timestamp time.Time        `json:"timestamp"`
	IsDelete  bool             `json:"isDelete"`
}

// QueryResult structure used for handling result of query
type QueryResult struct {
	Key    string `json:"Key"`
	Record *AccountOrderLog
}

// InitLedger adds a base set of cars to the ledger
func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	assets := []AccountOrderLog{
		{ID: "demo1", OrderID: "blue", PrevStatus: "5", Status: "Tomoko", Comment: "300", ReviewerID: "123", CreateTime: "2022-3-25", UpdateTime: "2022-3-25", CreateBy: "yulong", UpdateBy: "abe"},
		{ID: "demo2", OrderID: "blue2", PrevStatus: "52", Status: "Tomoko2", Comment: "3002", ReviewerID: "1232", CreateTime: "2022-3-25", UpdateTime: "2022-3-25", CreateBy: "yulong2", UpdateBy: "abe2"},
		{ID: "demo3", OrderID: "blue3", PrevStatus: "53", Status: "Tomoko3", Comment: "3003", ReviewerID: "1233", CreateTime: "2022-3-25", UpdateTime: "2022-3-25", CreateBy: "yulong3", UpdateBy: "abe3"},
	}

	for _, asset := range assets {
		assetJSON, err := json.Marshal(asset)
		if err != nil {
			return err
		}

		err = ctx.GetStub().PutState(asset.ID, assetJSON)
		if err != nil {
			return fmt.Errorf("failed to put to world state: %v", err)
		}
	}

	return nil
}

// CreateAsset issues a new asset to the world state with given details.
// id string, orderID string, prevStatus string, status string, comment string, reviewerID string, createTime string, updateTime string, createBy string, updateBy string
func (s *SmartContract) CreateAsset(ctx contractapi.TransactionContextInterface, id string, orderID string, prevStatus string, status string, comment string, reviewerID string, createTime string, updateTime string, createBy string, updateBy string) error {
	exists, err := s.AssetExists(ctx, id)
	if err != nil {
		return err
	}
	if exists {
		return fmt.Errorf("the asset %s already exists", id)
	}
	accountOrderLog := AccountOrderLog{
		ID:         id,
		OrderID:    orderID,
		PrevStatus: prevStatus,
		Status:     status,
		Comment:    comment,
		ReviewerID: reviewerID,
		CreateTime: createTime,
		UpdateTime: updateTime,
		CreateBy:   createBy,
		UpdateBy:   updateBy,
		// Features:   args[10],
	}

	assetJSON, err := json.Marshal(accountOrderLog)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(id, assetJSON)
}

// ReadAsset returns the asset stored in the world state with given id.
func (s *SmartContract) ReadAsset(ctx contractapi.TransactionContextInterface, id string) (*AccountOrderLog, error) {
	assetJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return nil, fmt.Errorf("failed to read from world state. %s", err.Error())
	}
	if assetJSON == nil {
		return nil, fmt.Errorf("the asset %s does not exist", id)
	}

	var accountOrderLog AccountOrderLog
	err = json.Unmarshal(assetJSON, &accountOrderLog)
	if err != nil {
		return nil, err
	}

	return &accountOrderLog, nil
}

// UpdateAsset updates an existing asset in the world state with provided parameters.
// id string, orderID string, prevStatus string, status string, comment string, reviewerID string, createTime string, updateTime string, createBy string, updateBy string
func (s *SmartContract) UpdateAsset(ctx contractapi.TransactionContextInterface, id string, orderID string, prevStatus string, status string, comment string, reviewerID string, createTime string, updateTime string, createBy string, updateBy string) error {
	exists, err := s.AssetExists(ctx, id)
	if err != nil {
		return err
	}
	if !exists {
		return fmt.Errorf("the asset %s does not exist", id)
	}

	// overwritting original asset with new asset
	accountOrderLog := AccountOrderLog{
		ID:         id,
		OrderID:    orderID,
		PrevStatus: prevStatus,
		Status:     status,
		Comment:    comment,
		ReviewerID: reviewerID,
		CreateTime: createTime,
		UpdateTime: updateTime,
		CreateBy:   createBy,
		UpdateBy:   updateBy,
		// Features:   args[10],
	}

	assetJSON, err := json.Marshal(accountOrderLog)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(id, assetJSON)
}

// DeleteAsset deletes an given asset from the world state.
func (s *SmartContract) DeleteAsset(ctx contractapi.TransactionContextInterface, id string) error {
	exists, err := s.AssetExists(ctx, id)
	if err != nil {
		return err
	}
	if !exists {
		return fmt.Errorf("the asset %s does not exist", id)
	}

	return ctx.GetStub().DelState(id)
}

// AssetExists returns true when asset with given ID exists in world state
func (s *SmartContract) AssetExists(ctx contractapi.TransactionContextInterface, id string) (bool, error) {
	assetJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return false, fmt.Errorf("failed to read from world state. %s", err.Error())
	}

	return assetJSON != nil, nil
}

// TransferAsset updates the owner field of asset with given id in world state.

// GetAllAssets returns all assets found in world state
func (s *SmartContract) GetAllAssets(ctx contractapi.TransactionContextInterface) ([]QueryResult, error) {
	// range query with empty string for startKey and endKey does an open-ended query of all assets in the chaincode namespace.
	resultsIterator, err := ctx.GetStub().GetStateByRange("", "")

	if err != nil {
		return nil, err
	}
	defer resultsIterator.Close()

	var results []QueryResult

	for resultsIterator.HasNext() {
		queryResponse, err := resultsIterator.Next()

		if err != nil {
			return nil, err
		}

		var accountOrderLog AccountOrderLog
		err = json.Unmarshal(queryResponse.Value, &accountOrderLog)
		if err != nil {
			return nil, err
		}

		queryResult := QueryResult{Key: queryResponse.Key, Record: &accountOrderLog}
		results = append(results, queryResult)
	}

	return results, nil
}

// GetAssetHistory returns the chain of custody for an asset since issuance.
func (t *SmartContract) GetAssetHistory(ctx contractapi.TransactionContextInterface, assetID string) ([]HistoryQueryResult, error) {
	log.Printf("GetAssetHistory: ID %v", assetID)

	resultsIterator, err := ctx.GetStub().GetHistoryForKey(assetID)
	if err != nil {
		return nil, err
	}
	defer resultsIterator.Close()

	var records []HistoryQueryResult
	for resultsIterator.HasNext() {
		response, err := resultsIterator.Next()
		if err != nil {
			return nil, err
		}

		var accountOrderLog AccountOrderLog
		if len(response.Value) > 0 {
			err = json.Unmarshal(response.Value, &accountOrderLog)
			if err != nil {
				return nil, err
			}
		} else {
			accountOrderLog = AccountOrderLog{
				ID: assetID,
			}
		}

		timestamp, err := ptypes.Timestamp(response.Timestamp)
		if err != nil {
			return nil, err
		}

		record := HistoryQueryResult{
			TxId:      response.TxId,
			Timestamp: timestamp,
			Record:    &accountOrderLog,
			IsDelete:  response.IsDelete,
		}
		records = append(records, record)
	}

	return records, nil
}

func main() {
	// See chaincode.env.example
	config := serverConfig{
		CCID:    os.Getenv("CHAINCODE_ID"),
		Address: os.Getenv("CHAINCODE_SERVER_ADDRESS"),
	}

	chaincode, err := contractapi.NewChaincode(&SmartContract{})

	if err != nil {
		log.Panicf("error create asset-transfer-basic chaincode: %s", err)
	}

	server := &shim.ChaincodeServer{
		CCID:    config.CCID,
		Address: config.Address,
		CC:      chaincode,
		TLSProps: shim.TLSProperties{
			Disabled: true,
		},
	}

	if err := server.Start(); err != nil {
		log.Panicf("error starting tcmp chaincode: %s", err)
	}
}
