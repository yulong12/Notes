'''
此程序用于生成学生成绩的散点图，横轴是序号，纵轴是成绩，并标出470和380的线
'''
import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# 从CSV文件中读取学生成绩数据
df = pd.read_csv('总表.csv')

# 创建散点图
fig = plt.figure()
plt.scatter(df.index, df['总折合分'])


plt.title('成绩散点图', fontsize=20)
plt.xlabel('序号',fontsize=16)
plt.ylabel('成绩',fontsize=16)

# 设置横轴刻度
plt.xticks(range(len(df.index)), df['班排'], rotation=90)
plt.yticks(range(0, 750, 50))


plt.axhline(y=470, color='r', linestyle='--', label='Score:470')
plt.text(len(df.index) + 1, 470, f'{470:.2f}', color='r')
plt.axhline(y=380, color='g', linestyle='--', label='Score:380')
plt.text(len(df.index) + 1, 380, f'{380:.2f}', color='g')

# 添加学生人数信息
grade_counts = df['总折合分'].value_counts().sort_index()
for grade, count in grade_counts.items():
    plt.text(grade, count, str(count), ha='center', va='bottom')

# 添加图例
plt.legend()

# 保存散点图为图片
plt.savefig('scatter_plot.png')

# 显示散点图
plt.show()