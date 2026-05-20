# Flask 待办事项应用

一个简洁的 Flask 待办事项应用，数据存储在内存中。

## 安装与运行

```bash
# 1. 创建并激活虚拟环境
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS / Linux

# 2. 安装依赖
pip install flask

# 3. 运行应用
python app.py
```

打开浏览器访问 `http://127.0.0.1:5000`。

## 功能

- 添加待办事项
- 标记完成 / 撤销完成
- 删除待办事项
- 显示完成进度统计
