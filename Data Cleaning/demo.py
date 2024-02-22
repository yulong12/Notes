import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.size'] = 12

# 从CSV文件中读取学生成绩数据
df = pd.read_csv('总表.csv')

# 创建散点图
fig = plt.figure()
plt.scatter(df.index, df['总折合分'])

# 添加标题和轴标签
plt.title('成绩散点图', fontsize=16)
plt.xlabel('序号')
plt.ylabel('成绩')

# 设置横轴刻度
plt.xticks(range(len(df.index)), df['姓名'], rotation=90)

# 设置纵轴刻度
plt.yticks(range(0, 101, 10))

# 计算平均分
mean = df['总折合分'].mean()

# 标识出平均分
plt.axhline(y=mean, color='r', linestyle='--', label='平均分')

# 添加平均分标签
plt.text(len(df.index) + 1, mean, f'平均分: {mean:.2f}', color='r')

# 标记位置为470和380的点
plt.annotate('470', xy=(470, df.loc[470, '总折合分']), xytext=(470, df.loc[470, '总折合分'] + 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), color='b')
plt.annotate('380', xy=(380, df.loc[380, '总折合分']), xytext=(380, df.loc[380, '总折合分'] - 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), color='b')

# 保存散点图为图片
plt.savefig('scatter_plot.png')

# 显示散点图
plt.show()