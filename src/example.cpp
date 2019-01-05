/*******************************************************************************
 * Copyright 2019, San. All rights reserved.
 * Author:  San
 * Date:    01/04/2019
 * Python API
 ******************************************************************************/
#include "example.h"
#include <sstream>

/*******************************************************************************
 * Example class
 ******************************************************************************/
Example::Example() {
    // m_people = std::make_unique<PersonDict>();
    m_people = new PersonDict();
    for (int i = 1; i <= 9; i++) {
        std::string id = std::to_string(i);
        (*m_people)[id] = new Person(id);
    }
    std::string programmer_id = "1000";
    (*m_people)[programmer_id] = new Programmer(programmer_id);
}

Example::~Example() {
    for (auto p : *m_people)
        delete p.second;
    delete m_people;
}

/*******************************************************************************
 * Person class
 * ****************************************************************************/
std::string Person::to_json() const {
    std::stringstream ss;

    ss << "{";
    ss << "\"id\":\"" << m_id << "\",";
    ss << "\"type\":\"Person\"";
    ss << "}";
    return ss.str();
}
