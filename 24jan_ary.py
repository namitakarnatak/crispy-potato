import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/stores/page/0F69EF02-570D-4C23-9298-EC855126D20E?store_ref=SB_A047185214YLG8YA1HV4L&pd_rd_w=5LEkA&pf_rd_p=278da5e5-bea3-4309-a099-569b9312a94e&pd_rd_wg=ZHVCG&pf_rd_r=S5KGAHVYW3FX1GDM2MJR&pd_rd_r=cd22c87b-4336-4400-89a7-3b0f43d8e2cc&aaxitk=.PVjzfnM4D-ijDkqha8g7Q&hsa_cr_id=9100690690602&lp_asins=B07V5FQBTQ%2CB07T1Z2H9S%2CB07SXG9P5C&lp_mat_key=biba%20for%20women&lp_query=womens&lp_slot=auto-sparkle-hsa-tetris&ref_=sbx_be_s_sparkle_tsld_bkgd&productGridPageIndex=4"
#url="https://www.myntra.com/dresses?f=Gender%3Amen%20women%2Cwomen"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)