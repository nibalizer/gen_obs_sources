import yaml
from jinja2 import Template, Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

d = yaml.safe_load(open("input.yaml"))

source_template = env.get_template("source.json.j2")
for source in d["browser_sources"]:
    #print(source['name'], source['url'])
    out = source_template.render(source=source)
    print(out)



