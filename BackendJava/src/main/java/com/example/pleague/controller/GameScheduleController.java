package com.example.pleague.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
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
@RequestMapping("api/gameschedule")
public class GameScheduleController {

    
    @Autowired
    private GameScheduleRepository gameScheduleRepository;

    @GetMapping
    public List<GameSchedule> getAllGameSchedules(
        @RequestParam(required = false) String year,
        @RequestParam(required = false) String gameType) {
            System.out.println("Received year: " + year);
            System.out.println("Received gameType: " + gameType);
        if (year != null && gameType != null) {
            return gameScheduleRepository.findByYearAndGameType(year, gameType);
        } else if (year != null) {
            return gameScheduleRepository.findByYear(year);
        } else if (gameType != null) {
            return gameScheduleRepository.findByGameType(gameType);
        } else {
            return gameScheduleRepository.findAll();
        }
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



