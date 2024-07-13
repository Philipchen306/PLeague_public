package com.example.pleague.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.pleague.model.Standings;

@Repository
public interface StandingsRepository extends JpaRepository<Standings, Integer> {
    List<Standings> findByYear(int year);
}
