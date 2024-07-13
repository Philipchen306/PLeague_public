package com.example.pleague.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.pleague.model.Standings;
import com.example.pleague.repository.StandingsRepository;

@RestController
@RequestMapping("/api/standings")
public class StandingsController {

    @Autowired
    private StandingsRepository standingsRepository;

    @GetMapping("/{year}")
    public List<Standings> getStandingsByYear(@PathVariable int year) {
        return standingsRepository.findByYear(year);
    }
}
