<<<<<<< HEAD
# xml_inspector
## About xml_inspector:
Displays the basic structure and attributes of a given XML document. This tool is particularly helpful when building XPaths. Note that this tool is not intended to troubleshoot malformed XML.

## Basic help information:
usage: xml_inspector.py [-h] xml_resource

positional arguments:
  xml_resource  File name or URL of the XML doc. URLs must start with "http"
                or "https"

optional arguments:
  -h, --help    show this help message and exit

## Example usage:

### Sample XML, pets.xml:
```
<pets>
  <cat type="American short hair">
    <age>7</age>
    <gender>male</gender>
    <fixed>true</fixed>
    <name>Eddie</name>
    <nickname>Edwardo</nickname>
    <nickname>Edwardeeto</nickname>
    <nickname>Edwardoritos</nickname>
  </cat>
  <cat type="Calico">
    <age>5</age>
    <gender>female</gender>
    <fixed>true</fixed>
    <name>Zoe</name>
    <nickname>Bean</nickname>
    <nickname>Zoe Bear</nickname>
  </cat>
  <cat type="Bombay">
    <age>6</age>
    <gender>male</gender>
    <fixed>true</fixed>
    <name>Danzig Sparta Warmachine</name>
    <nickname>Danzig</nickname>
    <nickname>D</nickname>
  </cat>
  <dog type="Mixed">
    <age>12</age>
    <gender>female</gender>
    <fixed>true</fixed>
    <name>Ebony</name>
    <nickname>Ebb</nickname>
  </dog>
</pets>
```

### Example usage:
```
user@linux$ python xml_inspector.py pets.xml
  pets: None ::   
    cat: type ::     
      age: None :: 7
      gender: None :: male
      fixed: None :: true
      name: None :: Eddie
      nickname: None :: Edwardo
      nickname: None :: Edwardeeto
      nickname: None :: Edwardoritos
    cat: type ::     
      age: None :: 5
      gender: None :: female
      fixed: None :: true
      name: None :: Zoe
      nickname: None :: Bean
      nickname: None :: Zoe Bear
    cat: type ::     
      age: None :: 6
      gender: None :: male
      fixed: None :: true
      name: None :: Danzig Sparta Warmachine
      nickname: None :: Danzig
      nickname: None :: D
    dog: type ::     
      age: None :: 12
      gender: None :: female
      fixed: None :: true
      name: None :: Ebony
      nickname: None :: Ebb
```

Just like Python, the level of indentation indicates the parent block of XML. For example, the parent of the `<cat>` tag is the `<pets>` tag and the output xml_inspector indents `cat:` more than `pets:` to reflect this fact.

Each row has three fields:
 * The first is the name of the XML tag (e.g. `<pets>` and `pets:`)
 * The second are any attributes that tag has (e.g. the `<cat>` and `<dog>` tags all have a `type` attribute). The text `None` will be shown if the tag has no attributes.
 * The third field is the (truncated) value between the start and end tags (e.g. the `true` in `<fixed>true</fixed>`

## Identifying XPaths:
Using the sample output, we can easily build XPaths to the information we want to target. For example, if we wanted to get the age of all the cats, we see that the heiarchy in the XML is `pets`, then `cat`, then age, making the XPath to the age value `/pets/cat/age/text()`.

If we wanted to get all the types of dogs, we can easily see the heiarchy is `pets`, `dog`, and the attribute `type` making the XPath `/pets/dog/@type`
=======
ME. (Perhaps I took the name of this file too literally.)
>>>>>>> 24a79e65d1eb7aa3a53a3edbd20f1e51736ac1fe
