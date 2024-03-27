use csv::Writer;
use std::error::Error;
use std::fs::File;

pub fn create_csv(filename: &str, data: &[Vec<&str>]) -> Result<(), Box<dyn Error>> {
    let file = File::create(filename)?;
    let mut writer = Writer::from_writer(file);

    for row in data {
        writer.write_record(row)?;
    }

    writer.flush()?;

    Ok(())
}
