from xml.etree import ElementTree as ET

def extract_failed_tests(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {"ns": "http://robotframework.org/robotml"}

    failed_tests = []
    for test in root.findall(".//ns:test", ns):
        name = test.attrib.get("name")
        status = test.find("ns:status", ns)
        if status is not None and status.attrib.get("status") == "FAIL":
            message = status.text
            failed_tests.append((name, message))

    return failed_tests

failed = extract_failed_tests("output.xml")
for name, msg in failed:
    print(f"Test échoué : {name} ⚠️ \nMessage : {msg}\n")
