from playwright.sync_api import sync_playwright

# 创建 PlaywrightContextManager 对象
playwright = sync_playwright()

# 访问 Chromium 浏览器实例
chromium = playwright.chromium

# 使用 Chromium 浏览器进行操作
browser = chromium.launch()

# 在此处添加你的代码，例如打开页面、操作页面元素等

# 关闭浏览器
browser.close()

# 关闭 PlaywrightContextManager 对象
playwright.stop()
