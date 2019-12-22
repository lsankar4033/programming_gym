use std::fmt;

const MIN_IN_HR: i32 = 60;
const MIN_IN_DAY: i32 = MIN_IN_HR * 24;

#[derive(Debug, PartialEq)]
pub struct Clock {
    total_min: i32,
}

fn positivify_min(m: i32) -> i32 {
    if m < 0 {
        return MIN_IN_DAY + m;
    } else {
        return m;
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            total_min: positivify_min((hours * 60 + minutes) % MIN_IN_DAY),
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock {
            total_min: positivify_min((self.total_min + minutes) % MIN_IN_DAY),
        }
    }

    fn hours(&self) -> i32 {
        self.total_min / MIN_IN_HR
    }

    fn minutes(&self) -> i32 {
        self.total_min - (self.hours() * MIN_IN_HR)
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours(), self.minutes())
    }
}
