import os
from langchain_groq import ChatGroq

# Set your API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize ChatGroq
llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",  
)
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

# Define prompt to generate restaurant name
def generate_restaurant_name_and_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest only one fancy name for a {cuisine} restaurant. Only give the name."
    )

    # Define prompt to generate menu items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 10 fancy menu items for a restaurant named {restaurant_name}. Only list the food menu items no explanations of the food items or no headings like Here are 10 fancy menu items in the begining too."
    )

    # Create the two LLMChains
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    name_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine them in a SequentialChain
    chain = SequentialChain(
        chains=[name_chain, name_items_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
        #verbose=True
    )

    # Run the chain
    response = chain({'cuisine': cuisine})
    return response

if(__name__=="__main__"):
    print(generate_restaurant_name_and_menu("Italian"))