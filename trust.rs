// Merry Christmas from Dark Sky Technology!

fn first_line(day_number: u32) {
    let day_name = match day_number {
        1 => "first",
        2 => "second",
        3 => "third",
        4 => "fourth",
        5 => "fifth",
        6 => "sixth",
        7 => "seventh",
        8 => "eighth",
        9 => "ninth",
        10 => "tenth",
        11 => "eleventh",
        12 => "twelfth",
        _ => "",
    };

    println!("\nOn the {} day of Christmas\nmy true love sent to me ",day_name);
}

fn gift(day_number: u32, prefix: &str) {
    let gift = match day_number {
        1 => "a Partridge in a Pear Tree",
        2 => "Two Turtle Doves",
        3 => "Three French Hens",
        4 => "Four Calling Birds",
        5 => "Five Golden Rings",
        6 => "Six Geese a Laying",
        7 => "Seven Swans a Swimming",
        8 => "Eight Maids a Milking",
        9 => "Nine Ladies Dancing",
        10 => "Ten Lords a Leaping",
        11 => "Eleven Pipers Piping",
        12 => "12 Drummers Drumming",
        _ => "",
    };

    println!("{}{}", prefix, gift);
}

fn main() {

    for day_number in 1..13 {
        first_line(day_number);

        for inner_day in (1..(day_number + 1)).rev() {
            gift(
                inner_day,
                if inner_day == 1 && day_number != 1 {
                    "and "
                } else {
                    ""
                },
            );
        }
    }
}
