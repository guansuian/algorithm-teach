# algorithm-teach

使用 Python 和 Manim 制作算法教学动画。项目目前处于初始化阶段。

## 环境

- Python 3.12.10
- Manim Community 0.22.0

## 安装

macOS 需要先准备 Cairo 和 pkg-config；使用 Homebrew 时可执行：

```bash
brew install cairo pkg-config
```

在项目目录创建虚拟环境并安装 Python 依赖：

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m manim --version
```

使用 `Tex`、`MathTex` 时还需要安装 LaTeX；普通图形和 `Text` 文字动画无需 LaTeX。

## 渲染动画

编写 Manim 场景后，可通过以下命令生成预览视频（替换文件名和场景类名）：

```bash
python -m manim -pql your_scene.py YourScene
```

虚拟环境、IDE 配置以及生成的 `media/` 文件不提交到 Git。
