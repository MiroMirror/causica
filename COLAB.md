# 在 Google Colab 中使用 Causica（Fork 版本）

本指南说明如何将修改后的 Causica fork 到自己的 GitHub，并在 Google Colab 中成功使用。

## 一、Fork 到你的 GitHub

### 1. 创建 Fork

1. 打开 [microsoft/causica](https://github.com/microsoft/causica)
2. 点击右上角 **Fork** 按钮
3. 选择你的 GitHub 账号作为目标

### 2. 推送本地修改到你的 Fork

若你已在本地完成修改，执行：

```bash
cd /path/to/causica

# 添加你的 fork 为 remote（将 YOUR_USERNAME 替换为你的 GitHub 用户名）
git remote add myfork https://github.com/YOUR_USERNAME/causica.git

# 推送 main 分支到你的 fork
git push myfork main
```

若你还没有 fork，可先 clone 原仓库再添加 remote：

```bash
git clone https://github.com/microsoft/causica.git
cd causica
git remote add myfork https://github.com/YOUR_USERNAME/causica.git
# ... 进行修改 ...
git add .
git commit -m "Support Python 3.10+ (including 3.13+)"
git push myfork main
```

---

## 二、在 Google Colab 中安装

### 方法 A：直接安装（推荐）

在 Colab 新建 notebook，第一个单元格执行：

```python
# 将 YOUR_GITHUB_USERNAME 替换为你的 GitHub 用户名
!pip install git+https://github.com/YOUR_GITHUB_USERNAME/causica.git
```

### 方法 B：指定分支

若你在其他分支（如 `python312`）开发：

```python
!pip install git+https://github.com/YOUR_USERNAME/causica.git@python312
```

### 方法 C：安装后重启运行时

若遇到依赖冲突，可先安装再重启：

```python
!pip install git+https://github.com/YOUR_USERNAME/causica.git
# 安装完成后：运行时 → 重新启动运行时
```

---

## 三、验证安装

在 Colab 中执行：

```python
import causica
print(causica.__version__)
```

若能看到版本号（如 `0.4.5`），说明安装成功。

---

## 四、运行示例

### 快速入门

建议先运行 [colab_quickstart.ipynb](examples/colab_quickstart.ipynb) 验证安装：

```
https://colab.research.google.com/github/YOUR_USERNAME/causica/blob/main/examples/colab_quickstart.ipynb
```

### 完整示例

- **多投资归因**：`examples/multi_investment_sales_attribution.ipynb`
- **CSuite 示例**：`examples/csuite_example.ipynb`

将 `YOUR_USERNAME` 替换为你的 GitHub 用户名即可在 Colab 中打开。

---

## 五、常见问题

### Q: Colab 提示 Python 版本不兼容？

本版本支持 **Python 3.10 及以上版本**（包括 3.10, 3.11, 3.12, 3.13 及未来版本）。Colab 当前多为 3.10，应可正常使用。可在 Colab 中执行 `!python --version` 查看版本。

### Q: 安装时 torch 版本冲突？

Colab 预装了 PyTorch。本包要求 `torch>=2.2.0`。若 pip 自动升级 torch 后出现异常，可尝试：

```python
# 先升级 torch，再安装 causica
!pip install "torch>=2.2.0"
!pip install git+https://github.com/YOUR_USERNAME/causica.git
```

然后 **运行时 → 重新启动运行时**。

### Q: 安装很慢或超时？

Colab 网络可能较慢。可多试几次，或使用 Colab Pro 的更好网络。

### Q: 想用私有仓库？

需先配置 GitHub 访问。可用 Personal Access Token：

```python
!pip install git+https://<YOUR_TOKEN>@github.com/YOUR_USERNAME/causica.git
```

注意：不要将 Token 提交到公开 notebook。

---

## 六、更新你的 Fork

当原仓库有更新时，可同步到你的 fork：

```bash
git remote add upstream https://github.com/microsoft/causica.git  # 仅首次需要
git fetch upstream
git merge upstream/main
git push myfork main
```

合并冲突时，需手动解决后再 push。
