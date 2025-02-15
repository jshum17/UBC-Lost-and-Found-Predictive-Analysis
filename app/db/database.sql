CREATE TABLE lost_items (
    id INT PRIMARY KEY,
    item_type VARCHAR(100),
    status VARCHAR(100),
    description TEXT,
    date_lost DATE,
    location VARCHAR(255)
);

-- DROP TABLE lost_items;
