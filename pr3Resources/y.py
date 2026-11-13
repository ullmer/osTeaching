import yaml
yfn = 'cspan-tags2.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)
