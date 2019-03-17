
from xml.etree.ElementTree import parse
from dict_xml import qytang_dict

tree = parse('XML_AutoWrite.xml')

root = tree.getroot()
department_list = []
for department in root.iter('部门'):
    department_dict = {'部门名': department.get('name')}
    for children in department.getchildren():
        children_list = []
        for x in children.getchildren():
            children_list.append(x.get('name'))
        department_dict[children.tag] = children_list
    department_list.append(department_dict)

qytang_dict_parser = {'公司': {'乾颐堂': {'部门': department_list}}}

if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)
    pp.pprint(qytang_dict_parser)



