package com.example.pleague.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Standings {

    @Id
    private int id;

    @Column(name = "team")
    private String team;

    @Column(name = "games_played")
    private int gamesPlayed;

    @Column(name = "wins")
    private int wins;

    @Column(name = "losses")
    private int losses;

    @Column(name = "pct")
    private String pct;

    @Column(name = "games_behind")
    private String gamesBehind;

    @Column(name = "streak")
    private String streak;

    @Column(name = "year")
    private int year;

    @Column(name = "rank")
    private int rank;

    // Constructors, getters, and setters

    public Standings() {
    }

    public Standings(int id, String team, int gamesPlayed, int wins, int losses, String pct, String gamesBehind, String streak, int year, int rank) {
        this.id = id;
        this.team = team;
        this.gamesPlayed = gamesPlayed;
        this.wins = wins;
        this.losses = losses;
        this.pct = pct;
        this.gamesBehind = gamesBehind;
        this.streak = streak;
        this.year = year;
        this.rank = rank;
    }

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getTeam() { return team; }
    public void setTeam(String team) { this.team = team; }
    public int getGamesPlayed() { return gamesPlayed; }
    public void setGamesPlayed(int gamesPlayed) { this.gamesPlayed = gamesPlayed; }
    public int getWins() { return wins; }
    public void setWins(int wins) { this.wins = wins; }
    public int getLosses() { return losses; }
    public void setLosses(int losses) { this.losses = losses; }
    public String getPct() { return pct; }
    public void setPct(String pct) { this.pct = pct; }
    public String getGamesBehind() { return gamesBehind; }
    public void setGamesBehind(String gamesBehind) { this.gamesBehind = gamesBehind; }
    public String getStreak() { return streak; }
    public void setStreak(String streak) { this.streak = streak; }
    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }
    public int getRank() { return rank; }
    public void setRank(int rank) { this.rank = rank; }
}
