package com.example.pleague.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.pleague.model.GameSchedule;


@Repository
public interface GameScheduleRepository extends JpaRepository<GameSchedule, Integer> {
    // List<GameSchedule> findByYearAndGameType(String year,String gameType); // Query method for year
    List<GameSchedule> findByYear(String year);
    List<GameSchedule> findByGameType(String gameType);
    List<GameSchedule> findByYearAndGameType(String year, String gameType);
    List<GameSchedule> findById(int id);
}


