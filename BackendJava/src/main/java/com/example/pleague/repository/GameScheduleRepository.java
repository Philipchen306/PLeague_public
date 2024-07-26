package com.example.pleague.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.pleague.model.GameSchedule;


@Repository
public interface GameScheduleRepository extends JpaRepository<GameSchedule, Long> {
    List<GameSchedule> findByYear(String year); // Query method for year
}


