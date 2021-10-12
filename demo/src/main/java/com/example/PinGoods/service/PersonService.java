package com.example.PinGoods.service;

//import com.example.PinGoods.dao.PersonDao;
import com.example.PinGoods.dao.personDao;
import com.example.PinGoods.model.person;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class PersonService {

    private final com.example.PinGoods.dao.personDao personDao;

    @Autowired
    public PersonService( @Qualifier("postgres") personDao personDao) {
        this.personDao = personDao;
    }

    public int addPerson(person person){
        return personDao.insertPerson(person);
    }

    public List<person> getAllPeople(){
        return personDao.selectAllPeople();
    }

    public Optional<person> getPersonById(UUID id){
        return personDao.selectPersonById(id);
    }

    public int deletePerson(UUID id){
        return personDao.deletePersonById(id);
    }

    public int updatePerson(UUID id, person newPerson){
        return personDao.updatePersonById(id,newPerson);
    }
}
