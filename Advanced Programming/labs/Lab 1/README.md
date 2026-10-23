ask: Parking Garage System
In Part A, you implement the basic classes at home. In Part B (during the lab session), you will extend your own classes from Part A, so follow the names and signatures below exactly.

1. Class Ticket
Create an abstract, immutable class Ticket representing a parking ticket for one vehicle.

Attributes:

private final String plate — the vehicle's license plate.

private final int minutes — the length of the stay in minutes.

Methods:

protected Ticket(String plate, int minutes) — a constructor that initializes the attributes. The license plate must not be null or an empty string, and the duration must be greater than 0. Throw IllegalArgumentException for invalid values.

public String getPlate() — returns the license plate.

public int getMinutes() — returns the duration in minutes.

public abstract double price() — returns the ticket price.

public String toString() — returns a string representation containing the license plate.

Note: All attributes must be private final. You must not add any set methods.

2. Class HourlyTicket
Create a class HourlyTicket that extends Ticket and represents a ticket with hourly billing.

Methods:

public HourlyTicket(String plate, int minutes) — a constructor that initializes the attributes through the Ticket constructor.

public double price() — returns the price based on the number of started hours. Each started hour costs 50.

Example: 60 minutes cost 50, while 61 minutes cost 100.

3. Class DailyTicket
Create a class DailyTicket that extends Ticket and represents a ticket with daily billing.

Methods:

public DailyTicket(String plate, int minutes) — a constructor that initializes the attributes through the Ticket constructor.

public double price() — returns the price based on the number of started days. Each started day costs 300, where one day is 1440 minutes.

4. Exception LotFullException
Create an exception class LotFullException that extends Exception, with a constructor LotFullException(). It is thrown only when there is no space left in the parking garage. After a failed attempt, the state of the garage must not change (the ticket count and revenue must remain the same).

5. Class ParkingLot
Create a class ParkingLot that stores parking tickets in an array.

Attributes:

private Ticket[] tickets — the array used to store tickets.

private int ticketCount — the number of tickets currently stored in the garage.

private int capacity — the capacity of the garage.

Methods:

public ParkingLot(int capacity) — a constructor that creates the array with the specified capacity. The capacity must be greater than 0; otherwise, throw IllegalArgumentException.

public void addTicket(Ticket ticket) throws LotFullException — adds a ticket to the garage. If the ticket is null, throw IllegalArgumentException. If the garage is full, throw LotFullException.

public int getTicketCount() — returns the number of tickets.

public double totalRevenue() — returns the total revenue, calculated as the sum of the prices of all added tickets. If the garage is empty, return 0.0.

Important: If an attempt to add a ticket fails, the state of the garage must not change. The ticket count and total revenue must remain the same.
