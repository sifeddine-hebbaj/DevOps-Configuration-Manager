from app import transform_to_yaml_with_xslt

if __name__ == "__main__":
    with open("test.xml", "r", encoding="utf-8") as f:
        xml_string = f.read()
    transform_to_yaml_with_xslt(
        xml_string,
        "xml2dockercompose.xslt",
        "generated_yamls/docker-compose.yml"
    )
    print("docker-compose.yml generated.") 