<p align="center">
    <img src="https://raw.githubusercontent.com/irgolic/orange3/README-shields/distribute/orange-title.png" alt="Orange 数据挖掘" height="200">
</p>
<p align="center">
    <b>Orange3 中文版 —— 开箱即用的中文数据挖掘与可视化平台</b>
</p>
<p align="center">
    <a href="https://github.com/xdfwsl/orange3">
        <img src="https://img.shields.io/badge/语言-中文-red" />
    </a>
    <a href="https://github.com/xdfwsl/orange3/releases">
        <img src="https://img.shields.io/github/v/release/biolab/orange3?label=基于版本" />
    </a>
    <a href="https://github.com/xdfwsl/orange3/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/biolab/orange3" />
    </a>
</p>

# Orange3 中文版

本项目是 [Orange3](https://github.com/biolab/orange3) 的**完整中文汉化版本**，基于 Orange3 上游主线开发，提供开箱即用的中文界面。

Orange 是一款面向初学者和专家的数据挖掘与可视化工具箱。使用 Orange 探索数据**无需编程或深入的数学知识**。通过基于工作流的拖拽式操作，任何拥有数据或对数据感兴趣的人都可以轻松上手。

<p align="center">
    <img src="https://raw.githubusercontent.com/irgolic/orange3/README-shields/distribute/orange-example-tall.png" alt="工作流示例">
</p>

## 汉化范围

| 模块 | 翻译条目 | 覆盖率 |
|------|---------|--------|
| Orange 组件 (widgets) | 3800+ | 91.5% |
| 菜单与对话框 (orangecanvas) | 470 | ~100% |
| 组件基础 UI (orangewidget) | 116 | 98.3% |

覆盖内容：
- **菜单栏**：文件、编辑、视图、选项、帮助等
- **组件面板**：数据、可视化、模型、评估、无监督学习
- **所有组件名称与描述**：文件、数据表、散点图、决策树、K-均值、测试与评分等
- **组件内部 UI**：按钮、标签、下拉选项、错误提示等
- **机器学习术语**：交叉验证、混淆矩阵、特征选择、正则化、梯度提升等

## 安装

### 方式一：Windows 直接安装（推荐新手使用）

适合没有 Python 基础的用户，下载即用：

1. 前往 [Releases](https://github.com/xdfwsl/orange3/releases) 页面下载最新的 **Orange3-Chinese-3.41.0-Windows-x86_64.exe** 安装包
2. 双击运行安装程序，按提示完成安装
3. 从桌面快捷方式或开始菜单启动 Orange3 中文版

### 方式二：在已有官方 Orange3 上汉化（最简单）

如果您已经通过[官方安装包](https://orange.biolab.si/download)安装了 Orange3，只需几步即可汉化：

```bash
# 用 pip 覆盖安装中文版（不影响已有数据和插件）
pip install git+https://github.com/xdfwsl/orange3.git

# 部署中文翻译
python -m Orange.i18n.setup_chinese
```

重新启动 Orange 即可看到中文界面。

### 方式三：pip 全新安装

```bash
# 安装 PyQt
pip install PyQt5 PyQtWebEngine
# 或 pip install PyQt6 PyQt6-WebEngine

# 从 GitHub 安装中文版
pip install git+https://github.com/xdfwsl/orange3.git

# 部署中文翻译
python -m Orange.i18n.setup_chinese
```

### 方式四：开发模式安装

```bash
git clone https://github.com/xdfwsl/orange3.git
cd orange3

pip install PyQt5 PyQtWebEngine
pip install -e .

# 部署中文翻译（首次安装必须执行）
python -m Orange.i18n.setup_chinese
```

### 方式五：Conda 安装

```bash
conda create python=3.12 --yes --name orange3
conda activate orange3
conda config --add channels conda-forge

# 先安装官方 Orange3
conda install orange3

# 然后覆盖安装中文版
pip install git+https://github.com/xdfwsl/orange3.git

# 部署中文翻译
python -m Orange.i18n.setup_chinese
```

## 启动

```bash
python -m Orange.canvas
```

首次启动会自动设置中文为默认语言。

常用启动参数：
```bash
# 跳过欢迎页，显示更多调试信息
python -m Orange.canvas -l 2 --no-splash --no-welcome

# 重置组件设置
python -m Orange.canvas --clear-widget-settings

# 深色模式
python -m Orange.canvas --style=fusion:breeze-dark
```

## 截图预览

安装完成后，您将看到完整的中文界面，包括：
- 中文菜单栏（文件、编辑、视图、选项、帮助）
- 中文组件面板（数据、可视化、模型、评估、无监督学习）
- 中文组件界面（所有按钮、标签、提示信息）

## 项目结构

```
Orange/i18n/
├── Chinese.json                 # Orange 组件中文翻译 (4164 条)
├── English.json                 # 英文原文 (对照)
├── orangecanvas_Chinese.json    # 菜单/对话框中文翻译 (470 条)
├── orangewidget_Chinese.json    # 组件基础 UI 翻译 (118 条)
├── setup_chinese.py             # 部署脚本
└── __init__.py

i18n/
├── zh/
│   ├── msgs.jaml                # trubar 翻译源文件 (16065 行)
│   └── tests-config.yaml
└── trubar-config.yaml           # 翻译配置
```

## 与上游同步

本项目会定期从 [biolab/orange3](https://github.com/biolab/orange3) 同步最新代码：

```bash
git remote add upstream https://github.com/biolab/orange3.git
git fetch upstream
git merge upstream/master
```

合并后如有新增字符串，可通过 trubar 工具补充翻译。

## 贡献

欢迎参与汉化改进！您可以：

1. **报告翻译问题** — 在 [Issues](https://github.com/xdfwsl/orange3/issues) 中指出翻译错误或遗漏
2. **提交翻译改进** — 直接编辑 `Orange/i18n/Chinese.json` 或 `i18n/zh/msgs.jaml`
3. **补充未翻译条目** — 目前仍有约 8% 的字符串等待翻译

### 翻译工具

项目使用 [trubar](https://pypi.org/project/trubar/) 翻译框架：

```bash
pip install trubar
cd i18n

# 提取需要翻译的字符串
trubar missing -c trubar-config.yaml zh Orange

# 应用翻译
trubar translate -c trubar-config.yaml zh Orange
```

## 致谢

- [Orange3](https://github.com/biolab/orange3) — 卢布尔雅那大学生物实验室开发的优秀开源数据挖掘平台
- [trubar](https://pypi.org/project/trubar/) — Orange 团队开发的国际化翻译工具

## 许可证

本项目与 Orange3 一样，采用 [GNU GPL v3.0](LICENSE) 许可证。
