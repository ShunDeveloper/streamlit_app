import pandas as pd

save_dir = 'data/'
ko_ron_df = pd.DataFrame(
  {
    '20':[float('nan'),float('nan'),float('nan'),float('nan')], 
    '25':[float('nan'),'1600','3200','6400'],
    '30':['1000','2000','3900','7700'],
    '40':['1300','2600','5200','8000'],
    '50':['1600','3200','6400','8000'],
    '60':['2000','3900','7700','8000'],
    '70':['2300','4500','8000','8000'],
    '80':['2600','1300','8000','8000'],
    '90':['2900','5800','8000','8000'],
    '100':['3200','6400','8000','8000'],
    '110':['3600','7100','8000','8000'],
  },
  index=[
    '1',
    '2',
    '3',
    '4'
  ]
)
ko_ron_df.to_csv(save_dir+'ko_ron.csv')

ko_tumo_df = pd.DataFrame(
  {
    '20':[float('nan'),'400-700','700-1300','1300-2600'], 
    '25':[float('nan'),float('nan'),'800-1600','1600-3200'],
    '30':['300-500','500-1000','1000-2000','2000-3900'],
    '40':['400-700','700-1300','1300-2600','2000-4000'],
    '50':['400-800','800-1600','1600-3200','2000-4000'],
    '60':['500-1000','1000-2000','2000-3900','2000-4000'],
    '70':['600-1200','1200-2300','2000-4000','2000-4000'],
    '80':['700-1300','1300-2600','2000-4000','2000-4000'],
    '90':['800-1500','1500-2900','2000-4000','2000-4000'],
    '100':['800-1600','1600-3200','2000-4000','2000-4000'],
    '110':['900-1800','1800-3600','2000-4000','2000-4000'],
  },
  index=[
    '1',
    '2',
    '3',
    '4'
  ]
)
ko_tumo_df.to_csv(save_dir+'ko_tumo.csv')

oya_ron_df = pd.DataFrame(
  {
    '20':[float('nan'),float('nan'),float('nan'),float('nan')], 
    '25':[float('nan'),'2400','4800','9600'],
    '30':['1500','2900','5800','11600'],
    '40':['2000','3900','7700','12000'],
    '50':['2400','4800','9600','12000'],
    '60':['2900','5800','11600','12000'],
    '70':['3400','6800','12000','12000'],
    '80':['3900','7700','12000','12000'],
    '90':['4400','8700','12000','12000'],
    '100':['4800','9600','12000','12000'],
    '110':['5300','10600','12000','12000'],
  },
  index=[
    '1',
    '2',
    '3',
    '4'
  ]
)
oya_ron_df.to_csv(save_dir+'oya_ron.csv')

oya_tumo_df = pd.DataFrame(
  {
    '20':[float('nan'),'700','1300','2600'], 
    '25':[float('nan'),float('nan'),'1600','3200'],
    '30':['500','1000','2000','3900'],
    '40':['700','1300','2600','4000'],
    '50':['800','1600','3200','4000'],
    '60':['1000','2000','3900','4000'],
    '70':['1200','2300','4000','4000'],
    '80':['1300','2600','4000','4000'],
    '90':['1500','2900','4000','4000'],
    '100':['1600','3200','4000','4000'],
    '110':['1800','3600','4000','4000'],
  },
  index=[
    '1',
    '2',
    '3',
    '4'
  ]
)
oya_tumo_df.to_csv(save_dir+'oya_tumo.csv')