/***********************************************************************
* Copyright 2019, San. All rights reserved.
* Author:  San
* Date:    01/04/2019
***********************************************************************/
#pragma once
#pragma warning (disable : 4251)
#include "export.h"
#include <string>
#include <vector>
#include <unordered_map>

class EXPORTED Person {
 public:
    Person() {}
    virtual ~Person() {}
    explicit Person(const std::string& id) : m_id(id) {}
    std::string         to_json() const;
    std::string         id() const                    { return m_id; }
    void                set_id(const std::string& id) { m_id = id; }
    virtual const char* type() const                  { return "Person"; }
    virtual std::string hello() const {
        return std::string("I am a person id ") + m_id;
    }

 protected:
    std::string m_id;
};

typedef std::vector<Person*>                     PersonList;
typedef std::unordered_map<std::string, Person*> PersonDict;

class EXPORTED Programmer : public Person {
 public:
    explicit Programmer(const std::string& id) : Person(id) {}
    virtual const char* type() const { return "Programmer"; }
    virtual std::string hello() const {
        return std::string("Programmer id ") + m_id;  // comment
    }
};

class EXPORTED Example {
 public:
    Example();
    virtual ~Example();

    const char  * hello() const { return "hello world"; }
    std::string   str() const   { return "Example object with 10 people"; }
    std::string   repr() const  { return "example.Example class"; }

    const Person* operator[](const std::string& id) const {
        if (has_person(id))
            return (*m_people)[id];
        return NULL;
    }

    bool has_person(const std::string& id) const {
        return m_people->find(id) != m_people->end();
    }

    PersonDict* people() { return m_people; }

 private:
    PersonDict* m_people;
};
