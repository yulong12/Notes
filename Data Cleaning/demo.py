import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['font.size'] = 12

# 从CSV文件中读取学生成绩数据
df = pd.read_csv('/Users/yulong/Documents/GitHub/New/Notes/Data Cleaning/Book1.csv')

# 创建散点图
fig = plt.figure()
print(df.index)
plt.scatter(df.index, df['总折合分'])

# pic = plt.plot(df['姓名'], df['总折合分'])


# 添加标题和轴标签
plt.title('成绩散点图', fontsize=16)
plt.xlabel('序号')
plt.ylabel('成绩')

# 设置横轴刻度
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
plt.xticks(range(len(df.index)),x, rotation=90)


# 设置纵轴刻度
plt.yticks(range(200, 600, 50))


# 计算平均分
mean = df['总折合分'].mean()

# 标识出平均分
# plt.axhline(y=mean, color='r', linestyle='--', label='平均分')

# 添加平均分标签
# plt.text(len(df.index) + 1, mean, f'平均分: {mean:.2f}', color='r')

# 标记位置为470和380的点
# plt.annotate('465', xy=(465, df.loc['姓名', 465]), xytext=(465, df.loc['姓名', 465] + 5),
#              arrowprops=dict(facecolor='black', arrowstyle='->'), color='b')
# plt.annotate('380', xy=(380, df.loc[380, '总折合分']), xytext=(380, df.loc[380, '总折合分'] - 10),
#              arrowprops=dict(facecolor='black', arrowstyle='->'), color='b')

plt.axhline(y=465, color='r', linestyle='--', label='特招线')
plt.text(len(df.index) + 1, 465, f'特招线', color='r')

plt.axhline(y=380, color='g', linestyle='--', label='本科线')
plt.text(len(df.index) + 1, 380, f'本科线', color='g')



# plt.axhline(y=380, color='g', linestyle='--', label='380线')
# plt.text(len(df.index) + 1, 380, f'380线: {380:.2f}', color='g')

# plt.annotate('380', xy=('姓名', 500), xytext=('姓名', 500),
#              arrowprops=dict(facecolor='black', arrowstyle='->'), color='b')
# s, xy, *args, **kwargs
plt.grid
# 保存散点图为图片
plt.savefig('scatter_plot.png')

# 显示散点图
plt.show()