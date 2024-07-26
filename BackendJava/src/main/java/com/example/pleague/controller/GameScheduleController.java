package com.example.pleague.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.pleague.model.GameSchedule;
import com.example.pleague.repository.GameScheduleRepository;

// @RestController
// @RequestMapping("/api/schedules")
// @CrossOrigin(origins = "http://localhost:3000")
// public class GameScheduleController {

//     @Autowired
//     private GameScheduleRepository gameScheduleRepository;

//     @GetMapping
//     public List<GameSchedule> getAllGameSchedules() {
//         return gameScheduleRepository.findAll();
//     }

//     @PostMapping
//     public GameSchedule saveGameSchedule(@RequestBody GameSchedule gameSchedule) {
//         return gameScheduleRepository.save(gameSchedule);
//     }
// }

@RestController
@RequestMapping("/api/schedules")
public class GameScheduleController {

    @Autowired
    private GameScheduleRepository gameScheduleRepository;

    @GetMapping("/{year}")
    public List<GameSchedule> getSchedulesByYear(@PathVariable String year) {
        return gameScheduleRepository.findByYear(year);
    }

    @PostMapping
    public GameSchedule addSchedule(@RequestBody GameSchedule schedule) {
        return gameScheduleRepository.save(schedule);
    }
}