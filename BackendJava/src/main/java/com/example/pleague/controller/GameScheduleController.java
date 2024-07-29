package com.example.pleague.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
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
public class GameScheduleController {
    @Autowired
    private GameScheduleRepository gameScheduleRepository;

    @GetMapping("/game-schedule")
    public List<GameSchedule> getGameScheduleByYearAndType(@RequestParam String year, @RequestParam String gameType) {
        return gameScheduleRepository.findByYearAndGameType(year, gameType);
    }
}

// @RequestMapping("/games")
// public class GameScheduleController {

//     @Autowired
//     private GameScheduleRepository gameScheduleRepository;

//     @GetMapping
//     public List<GameSchedule> getSchedulesByYear() {
//         return gameScheduleRepository.findAll();
//     }

//     @GetMapping("/game-schedule")
//     public List<GameSchedule> getGamesByYearAndType(@RequestParam String year, @RequestParam String gameType) {
//         return gameScheduleRepository.findYearAndGameType(year,gameType);
//     }
//     }


    // @PostMapping
    // public GameSchedule addSchedule(@RequestBody GameSchedule schedule) {
    //     return gameScheduleRepository.save(schedule);
    // }



