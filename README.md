# rating-system-adapter

Rating System 各大 OJ 平台适配器（实验仓库）。

## 适配器列表

| 适配器网站 | 账户验证 | 状态抓取 | 题目抓取 |
| --- | --- | --- | --- |
| [Luogu](https://www.luogu.com.cn/) | 是 | 否 | 否 |

## 使用说明

请将需要的适配器的所有文件移动到 [Rating System](https://github.com/ZnPdCo/rating-system) 的 `backend/app/custom` 文件夹下，重启 Rating System 后生效。

部分适配器可能需要相关环境，详见各适配器目录下 README 中的 `环境` 部分。部分适配器支持自定义配置，相关配置选项可以在 `backend/app/config.py` 中修改。