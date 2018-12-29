#pragma once
#include <string>
#include <vector>
#include <map>
#include "export.h"

class Person;

class EXPORTED Example {
public:
    Example();
    ~Example(){}
    const char *hello() const;
    std::string str() const { return "Example with people";}
    std::string repr() const { return "example.Example class";}
    std::vector<Person*> * people() {return m_people;}
    std::map<std::string, Person*> * peope_map() {return m_people_map; }
    Person* person() const { return m_person; }
    Person* operator[] (const std::string& id) {
        return (*m_people_map)[id];
    }
private:
    Person* m_person;
    std::vector<Person*> * m_people;
    std::map<std::string, Person*> * m_people_map;
};


