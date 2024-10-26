def allocate(tasks,num,maxLoad):
    loads=[0]*num
    allocate_types=[set() for _ in range(num)]
    sorted_taskes=sorted(tasks.items(),key=lambda x:x[1],reverse=True)
    for tasks_type,task_count in sorted_taskes:
        allocate=False
        for i in range(num):
            if tasks_type not in allocate_types[i] and loads[i]+task_count<=maxLoad:
                loads[i]+=task_count
                allocate_types[i].add(tasks_type)
                allocate=True
                break
            if not allocate:
                return False
    return True
def minMaxLoad(tasks,nunmber):
    total_tasks=sum(tasks.values())
    left,right=0,total_tasks
    while left<right:
        mid=(left+right)//2
        if allocate(tasks,nunmber,mid):
            right=mid
        else:
            left=mid+1
    return left
tasks={0:5,1:2}
print(minMaxLoad(tasks,5))
    
                