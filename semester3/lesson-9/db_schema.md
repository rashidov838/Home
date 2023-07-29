Table store {
  id integer [pk]   
  name varchar(50)
  address varchar(100)
  phone varchar(100)
  map_link varchar(100)
  description varchar(200)
  start_time timestamp
  end_time timestamp
}

Table category {
  id integer [pk]
  name varchar(50)
  description varchar(50)
}

Table product {
  id integer [pk]
  name varchar(100)
  desciption varchar(200)
  created_at timestamp
  price money
  rating decimal
  company_name varchar(50)
  quantity decimal
  // category_id
  // seller_id 

}

Table seller {
  id integer [pk]
  first_name varchar(50) 
  last_name varchar(50)
  age integer
  rating decimal
  // 
  work_start_time timestamp  
  work_end_time timestamp
  trading_exp varchar(20)
  password varchar(20)
  email varchar(100)
  date_of_birth date
}

Table purchase {
  id integer [pk]
  list_products varchar(100)
  quantity integer
  total_price money
  customer varchar(20)
  seller varchar(20)
  created_at timestamp
  
}

Table sell {
  id integer [pk]
  name varchar(50)
  quantity integer
  total_price decimal
  seller varchar(100)
  customer varchar(100)
  cash boolean
  card boolean
  discount decimal
  created_at timestamp

}

Table manufacturer {
  id integer [pk]
  name varchar(20)
  desciption varchar(20)
  address varchar(50)
  email varchar(100)
  telephone varchar(200)
  map_link varchar(200)
  rating decimal
}

Table customer {
  id integer [pk]
  first_name varchar(50)
  last_name varchar(50)
  age integer
  email varchar(100)
  password varchar(30)
  date_of_birth date
  cash decimal
  card decimal
  discount decimal
}

Table bucket {
  id integer [pk]  
}

Table review {
  id integer [pk]   
  rating decimal
  comment varchar(40)
  donation boolean
  created_at date
}
