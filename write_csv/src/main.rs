mod csv_writer;

fn main() {
    let data = vec![
        vec!["Name", "Age", "City"],
        vec!["Alice", "25", "New York"],
        vec!["Bob", "30", "London"],
        vec!["Charlie", "35", "Paris"],
        vec!["Émilie", "28", "Lyon"],
        vec!["山田", "40", "東京"],
    ];

    match csv_writer::create_csv("./data/from_rust.csv", &data) {
        Ok(_) => println!("CSV file created successfully."),
        Err(e) => println!("Error creating CSV file: {}", e),
    }
}

