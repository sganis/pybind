#include "example.h"
#include "person.h"

Example::Example()
{
    m_person = new Person("0");
    m_people = new std::vector<Person*>;
    m_people_map = new std::map<std::string, Person*>;
    for (int i=1; i<=10; i++) {
        std::string id = std::to_string(i);
        Person* p = new Person(id);
        m_people->push_back(p);
        (*m_people_map)[id] = p;
    }
}

const char* Example::hello() const
{
    return "hello world";
}


