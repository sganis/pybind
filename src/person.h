#pragma once
#include <string>

class Person {
public:
    Person();
    Person(const std::string& id){m_id = id;}
    std::string hello() const {
        std::string s = "I am a person id " + m_id;
        return s;
    }

private:
    std::string m_id;
};



