%%R
# Basic arithmetic operations in R
a <- 10
b <- 5

# Addition
sum_result <- a + b
cat("Sum:", sum_result, "\n")

# Subtraction
sub_result <- a - b
cat("Subtraction:", sub_result, "\n")

# Multiplication
mul_result <- a * b
cat("Multiplication:", mul_result, "\n")

# Division
div_result <- a / b
cat("Division:", div_result, "\n")

# Conditional
if (a > b) {
  cat("a is greater than b\n")
} else {
  cat("b is greater than or equal to a\n")
}


# Define a vector of numbers
numbers <- c(10, 20, 30, 40, 50)

# Calculate basic statistics
mean_value <- mean(numbers)
median_value <- median(numbers)

# Print the mean and median
print(paste("Mean:", mean_value))
print(paste("Median:", median_value))

# Create a data frame
df <- data.frame(
  Name = c("Alice", "Bob", "Charlie"),
  Age = c(24, 27, 22),
  Course = c("BDA", "ML", "AI")
)

# View the data frame
print(df)

# Filter the data frame to find students older than 23
filtered_df <- subset(df, Age > 23)
print(filtered_df)


# to run : Rscript my_script.R


# R is a powerful language and environment for statistical computing and graphics. It allows you to work with vectors, data frames, and other data structures to perform analysis and basic operations.

# R Scripts can perform tasks like:
# Defining vectors and performing arithmetic on them.
# Creating data frames for structured data.
# Filtering data using conditions.
# Basic statistics like mean, median, etc.

