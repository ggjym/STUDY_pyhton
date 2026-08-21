name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily_growth_factor=1.2
growth_days=7
print("公司%s，股票代码：%s，当前股价：%.2f\n每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f"
      %(name,stock_code,stock_price,stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor*growth_days))