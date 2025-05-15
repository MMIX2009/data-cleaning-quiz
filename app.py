import streamlit as st

# Title of the app
st.title("Pandas Data Cleaning & Preparation Quiz")
st.write("📊 Master Your Data Cleaning Skills with Pandas!")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Pandas Data Cleaning MCQ Quiz (Merged 40 Questions)
quiz = [
    {"question": "What percentage of time is typically spent on data cleaning and preparation in the data analysis lifecycle?",
     "options": ["50%", "60%", "70%", "80%"],
     "answer": "80%"},

    {"question": "Which of the following is NOT a key step in data cleaning and preparation?",
     "options": ["Loading data", "Handling missing data", "Data encryption", "Transforming data"],
     "answer": "Data encryption"},

    {"question": "Which two values represent missing data in pandas?",
     "options": ["None and NaN", "NA and NaN", "Null and None", "NA and Null"],
     "answer": "NA and NaN"},

    {"question": "Which pandas method removes rows or columns containing missing values?",
     "options": ["fillna()", "dropna()", "replace()", "remove()"],
     "answer": "dropna()"},

    {"question": "How can you fill missing values in different columns with different values?",
     "options": ["Use a dictionary with fillna()", "Use dropna() with axis=1", "Use replace() directly", "Use map() function"],
     "answer": "Use a dictionary with fillna()"},

    {"question": "Which method fills missing values with the last observed non-NA value?",
     "options": ["dropna()", "fillna()", "ffill()", "backfill()"],
     "answer": "ffill()"},

    {"question": "What method returns a boolean Series indicating duplicate rows?",
     "options": ["drop_duplicates()", "duplicated()", "is_duplicate()", "remove_duplicates()"],
     "answer": "duplicated()"},

    {"question": "How can you remove duplicates based on a subset of columns?",
     "options": ["duplicated(subset=...)", "drop_duplicates(subset=...)", "remove_duplicates(columns=...)", "dropna(subset=...)"],
     "answer": "drop_duplicates(subset=...)"},

    {"question": "Which method applies element-wise transformations using a function or dictionary?",
     "options": ["map()", "replace()", "apply()", "transform()"],
     "answer": "map()"},

    {"question": "Which method is used for replacing multiple values in a Series or DataFrame?",
     "options": ["replace()", "map()", "rename()", "dropna()"],
     "answer": "replace()"},

    {"question": "Which pandas function is used to bin continuous data into specified intervals?",
     "options": ["cut()", "qcut()", "binning()", "bucketize()"],
     "answer": "cut()"},

    {"question": "How does pandas.qcut() divide data into bins?",
     "options": ["Based on specified bin edges", "Based on sample quartiles", "Randomly", "Based on mean and median values"],
     "answer": "Based on sample quartiles"},

    {"question": "How can outliers be detected and filtered out using pandas?",
     "options": ["Using np.sign()", "Using dropna()", "Using pd.get_dummies()", "Using fillna() with median"],
     "answer": "Using np.sign()"},

    {"question": "What is a more Pythonic way to concatenate strings from a list with a '::' separator?",
     "options": ["Using the '+' operator", "Using join()", "Using split()", "Using format()"],
     "answer": "Using join()"},

    {"question": "Which string method returns the number of occurrences of a substring?",
     "options": ["find()", "count()", "index()", "locate()"],
     "answer": "count()"},

    {"question": "How do you convert a pandas DataFrame column to a categorical type?",
     "options": ["astype('category')", "convert('category')", "categorize()", "set_type('category')"],
     "answer": "astype('category')"},

    {"question": "Which function performs one-hot encoding of categorical variables in pandas?",
     "options": ["pd.get_dummies()", "pd.categorize()", "pd.one_hot()", "pd.encode()"],
     "answer": "pd.get_dummies()"},

    {"question": "How can you access the category codes after converting a column to categorical?",
     "options": ["df.cat.codes", "df.categories", "df.codes", "df.get_codes()"],
     "answer": "df.cat.codes"},

    {"question": "Which pandas method can be used to rename index values using a function?",
     "options": ["rename()", "reindex()", "map()", "set_index()"],
     "answer": "rename()"},

    {"question": "Which parameter in dropna() ensures that only rows where all values are missing are dropped?",
     "options": ["how='any'", "how='all'", "axis=1", "thresh=1"],
     "answer": "how='all'"},

    {"question": "Which dropna() parameter is used to drop columns instead of rows?",
     "options": ["axis=0", "axis=1", "how='columns'", "inplace=True"],
     "answer": "axis=1"},

    {"question": "What does the 'thresh' parameter in dropna() control?",
     "options": ["The number of NA values allowed", "The minimum number of non-NA values required", 
                  "The type of NA values to drop", "Whether to drop rows or columns"],
     "answer": "The minimum number of non-NA values required"},

    {"question": "Which method replaces NA values with the mean of a Series?",
     "options": ["fillna(df.mean())", "dropna(mean=True)", "replace(mean=True)", "fillna('mean')"],
     "answer": "fillna(df.mean())"},

    {"question": "How can you limit the number of consecutive missing values filled using ffill()?",
     "options": ["Use limit parameter", "Use max parameter", "Set axis=1", "Use how='all'"],
     "answer": "Use limit parameter"},

    {"question": "What is the result of using fillna(inplace=True)?",
     "options": ["A new DataFrame is returned", "Original DataFrame is modified directly", 
                 "A copy of the DataFrame is created", "It has no effect"],
     "answer": "Original DataFrame is modified directly"},

    {"question": "Which function returns a special Categorical object for discretized data?",
     "options": ["cut()", "categorize()", "qcut()", "binning()"],
     "answer": "cut()"},

    {"question": "Which method displays which bin each data point belongs to after using cut()?",
     "options": ["df.categories", "df.codes", "df.bins", "df.labels"],
     "answer": "df.codes"},

    {"question": "Which method is used to count the number of data points in each bin?",
     "options": ["pd.count_bins()", "pd.bin_counts()", "pd.value_counts()", "pd.bin_stats()"],
     "answer": "pd.value_counts()"},

    {"question": "How do you automatically divide data into equal number of elements using cut?",
     "options": ["Use qcut", "Use cut with equal_bins=True", "Use cut with integer for bins", "Use pd.equalize()"],
     "answer": "Use cut with integer for bins"},

    {"question": "Which method helps detect outliers by checking values greater than a threshold along any axis?",
     "options": ["any()", "all()", "np.sign()", "is_outlier()"],
     "answer": "any()"},

    {"question": "Which NumPy function returns the sign (+1, -1) of values in an array?",
     "options": ["np.sign()", "np.abs()", "np.positive()", "np.check_sign()"],
     "answer": "np.sign()"},

    {"question": "Which string method removes leading and trailing whitespace from a string?",
     "options": ["trim()", "strip()", "split()", "replace()"],
     "answer": "strip()"},

    {"question": "Which string method is used to locate the position of a substring within a string?",
     "options": ["index()", "position()", "locate()", "split()"],
     "answer": "index()"},

    {"question": "Which string method returns -1 if the substring is not found, instead of raising an error?",
     "options": ["index()", "find()", "search()", "count()"],
     "answer": "find()"},

    {"question": "What happens when you pass an empty string to the replace() method in a string?",
     "options": ["It raises an error", "Deletes the original term", "Replaces all values with NaN", "Nothing changes"],
     "answer": "Deletes the original term"},

    {"question": "Which method is used to split a string into a list of substrings based on a delimiter?",
     "options": ["split()", "partition()", "extract()", "separate()"],
     "answer": "split()"},

    {"question": "Which pandas function converts categorical data into binary indicator variables?",
     "options": ["pd.categorize()", "pd.one_hot()", "pd.get_dummies()", "pd.encode_categories()"],
     "answer": "pd.get_dummies()"},

    {"question": "What is the purpose of Cat.categories in pandas?",
     "options": ["Returns numerical category codes", "Lists unique category labels", 
                 "Counts the number of categories", "One-hot encodes categories"],
     "answer": "Lists unique category labels"},

    {"question": "Which method would you use to rename row indices directly in a DataFrame?",
     "options": ["map()", "rename()", "reindex()", "set_index()"],
     "answer": "rename()"}
]

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio(
    "Select your answer:",
    current_question["options"],
    key=f"question_{st.session_state.question_index}"
)

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Incorrect. The correct answer is: **{current_question['answer']}**")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            st.rerun()  # Force rerun to display the next question immediately
        else:
            st.balloons()
            st.write("🎉 **Quiz Completed!**")
            st.write(f"Your final score is **{st.session_state.score}/{len(quiz)}**")
            # Reset for new attempt
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")
