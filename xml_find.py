
from xml.etree.ElementTree import parse
from dict_xml import qytang_dict

tree = parse('XML_AutoWrite.xml')

root = tree.getroot()

department_list = []
for department in root.iter('部门'):
    department_dict = {'部门名': department.get('name')}

    teachers_list = []
    for teacher in department.iter('老师'):
        teachers_list.append(teacher.get('name'))
    department_dict['师资'] = teachers_list

    courses_list = []
    for course in department.iter('课程名'):
        courses_list.append(course.get('name'))
    department_dict['课程'] = courses_list
    department_list.append(department_dict)

qytang_dict_parser = {'公司': {'乾颐堂': {'部门': department_list}}}

if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qytang_dict)
    pp.pprint(qytang_dict_parser)

