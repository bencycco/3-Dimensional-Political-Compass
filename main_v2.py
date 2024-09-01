test_dict = {
        1: {"question": "Hello", "weight": 1},
        2: {"question": "How are You", "weight": 2}
}

culture_questions = {
        1: {"question": "People should follow traditional customs and practices.", "weight": 2, "right": True},
        2: {"question": "It is important to celebrate national holidays and symbols.", "weight": 1, "right": True},
        3: {"question": "Learning about different cultures is important for everyone.", "weight": 2, "right": False},
        4: {"question": "Family values should be taught in schools.", "weight": 3, "right": True},
        5: {"question": "Modern technology has a positive impact on society.", "weight": 1, "right": False},
        6: {"question": "Respecting elders is more important than questioning them.", "weight": 3, "right": True},
        7: {"question": "All people should be free to express their religious beliefs.", "weight": 2, "right": False},
        8: {"question": "Schools should focus on teaching students about their country’s history.", "weight": 2, "right": True},
        9: {"question": "Art and music from all cultures should be appreciated", "weight": 2, "right": False},
        10: {"question": "It is important to dress modestly in public.", "weight": 3, "right": True},
        11: {"question": "People should have the freedom to choose their lifestyle.", "weight": 3, "right": False},
        12: {"question": "Students should learn to follow rules without question.", "weight": 2, "right": True},
        13: {"question": "Movies and video games should be censored to protect children.", "weight": 3, "right": True},
        14: {"question": "Public statues of historical figures should be preserved.", "weight": 2, "right": True},
        15: {"question": "Cultural traditions should adapt to modern times.", "weight": 2, "right": False},
        16: {"question": "Parents should decide what their children learn about society.", "weight": 3, "right": True},
        17: {"question": "Everyone should celebrate their cultural heritage.", "weight": 1, "right": False},
        18: {"question": "People should speak the official language of their country in public places.", "weight": 2, "right": True},
        19: {"question": "Schools should teach students how to think critically about their culture.", "weight": 2, "right": False},
        20: {"question": "Gender roles are important for a stable society.", "weight": 3, "right": True},
        21: {"question": "People should avoid offending others with their opinions.", "weight": 3, "right": True}
}
economy_questions = {
        1: {"question": "Businesses should be free to make their own decisions without government interference.", "weight": 2, "right": True},
        2: {"question": "The government should make sure everyone has access to basic needs like food and shelter.", "weight": 2, "right": False},
        3: {"question": "People who work hard should keep most of the money they earn.", "weight": 2, "right": True},
        4: {"question": "Wealth should be shared more equally among everyone in society.", "weight": 3, "right": False},
        5: {"question": "Taxes should be low to encourage people to work and invest.", "weight": 3, "right": True},
        6: {"question": "Big businesses should be taxed more to help fund public services.", "weight": 2, "right": False},
        7: {"question": "People should have the freedom to start their own businesses.", "weight": 1, "right": True},
        8: {"question": "The government should help people who are unemployed.", "weight": 2, "right": False},
        9: {"question": "It’s fair for people to earn more money if they work harder.", "weight": 2, "right": True},
        10: {"question": "Healthcare should be provided by the government for everyone.", "weight": 3, "right": False},
        11: {"question": "People should be allowed to make as much money as they can.", "weight": 2, "right": True},
        12: {"question": "Public transportation should be free for everyone.", "weight": 3, "right": False},
        13: {"question": "There should be rules to protect the environment, even if it costs businesses money.", "weight": 2, "right": False},
        14: {"question": "Rich people should pay more in taxes than poor people.", "weight": 2, "right": False},
        15: {"question": "People should be responsible for their own financial well-being.", "weight": 3, "right": True},
        16: {"question": "Education should be free for everyone.", "weight": 3, "right": True},
        17: {"question": "The government should help small businesses compete with big companies.", "weight": 2, "right": False},
        18: {"question": "Prices of goods should be decided by the market, not the government.", "weight": 3, "right": True},
        19: {"question": "The minimum wage should be high enough to support a family.", "weight": 2, "right": False},
        20: {"question": "There should be no limits on how much wealth a person can have.", "weight": 2, "right": True},
        21: {"question": "Public services like water and electricity should be controlled by the government.", "weight": 2, "right": False},
        22: {"question": "People should be rewarded based on their talents and efforts, not just their needs.", "weight": 3, "right": True}
}

authority_questions = {
        1: {"question": "People should be free to say whatever they want, even if it offends others.", "weight": 3, "right": False},
        2: {"question": "The government should have the power to keep people safe, even if it means some freedoms are limited.", "weight": 2, "right": True},
        3: {"question": "Everyone should have the right to privacy, even from the government.", "weight": 2, "right": False},
        4: {"question": "Police should have the power to search people’s homes if they suspect illegal activity.", "weight": 1, "right": True},
        5: {"question": "People should be free to protest and criticize the government.", "weight": 2, "right": False},
        6: {"question": "The government should be allowed to monitor people to prevent crime.", "weight": 3, "right": True},
        7: {"question": "Freedom of speech is more important than keeping people from being offended.", "weight": 2, "right": False},
        8: {"question": "The government should have strict rules to keep everyone safe.", "weight": 2, "right": True},
        9: {"question": "People should be free to practice any religion they choose.", "weight": 2, "right": False},
        10: {"question": "It’s important to obey laws, even if they seem unfair.", "weight": 2, "right": True},
        11: {"question": "Everyone should be treated equally by the government, no matter who they are.", "weight": 1, "right": False},
        12: {"question": "People should have the right to own weapons to protect themselves.", "weight": 2, "right": False},
        13: {"question": "The government should be able to control the internet to stop harmful content.", "weight": 2, "right": True},
        14: {"question": "Freedom of the press is important, even if it means some information is upsetting.", "weight": 3, "right": False},
        15: {"question": "The government should not interfere with people’s personal lives.", "weight": 2, "right": False},
        16: {"question": "People should have the right to choose how they want to live.", "weight": 1, "right": False},
        17: {"question": "There should be laws to protect people from harmful speech.", "weight": 3, "right": True},
        18: {"question": "People should be allowed to move freely within their country and across borders.", "weight": 2, "right": False},
        19: {"question": "The government should be able to take private property for public use if it’s necessary.", "weight": 3, "right": True},
        20: {"question": "People should have the freedom to choose what they want to learn in school.", "weight": 1, "right": False},
        21: {"question": "The government should respect everyone’s rights, even if it makes things harder to manage.", "weight": 2, "right": False}
}

scores = {
    "Culture": 0,
    "Economy": 0,
    "Liberty": 0
}

def axis_calc(questions):
    i = 1
    axis = 0
    for question in questions.items():
        response = float(input(f"""
{questions[i]["question"]}
              1) Strongly Disagree
              2) Disagree
              3) Neutral
              4) Agree
              5) Strongly Agree
        > """))

        if questions[i]["right"]:
            if response == 1:
                axis = axis - (2 * questions[i]["weight"])
            elif response == 2:
                axis = axis - (1 * questions[i]["weight"])
            elif response == 4:
                axis = axis + (1 * questions[i]["weight"])
            elif response == 5:
                axis = axis + (2 * questions[i]["weight"])
        else:
            if response == 1:
                axis = axis + (2 * questions[i]["weight"])
            elif response == 2:
                axis = axis + (1 * questions[i]["weight"])
            elif response == 4:
                axis = axis - (1 * questions[i]["weight"])
            elif response == 5:
                axis = axis - (2 * questions[i]["weight"])

        i += 1
    return axis

def explain(cult, econ, auth):
    # Explaining their cultural axis
    print("-----CULTURE-----")
    print(f"Your cultural axis is {cult / 2}\n")
    if (cult / 2) > 0:
        if (cult / 2) <= 15:
            print("You are Culturally Centre-Right.")
            print("Culturally center-right refers to a perspective that values traditional cultural norms and practices, emphasizing the importance of preserving established customs and institutions.")
            print("This viewpoint often supports gradual change rather than radical reforms, prioritizing stability and continuity in societal values.")
        elif (cult / 2) < 30:
            if (cult / 2) > 15:
                print("You are Culturally Right-Wing.")
                print("Culturally right-wing refers to a viewpoint that strongly emphasizes traditional cultural norms and values, often advocating for a return to or preservation of these longstanding practices.")
                print("This perspective typically resists progressive changes and seeks to uphold established social structures and cultural identities.")
        else:
            print("You are Culturally Far-Right.")
            print("Culturally far-right refers to a perspective that advocates for a strict adherence to traditional cultural norms and values, often with an exclusionary approach towards those who deviate from or challenge these norms.")
            print("This viewpoint tends to promote a homogeneous cultural identity and can be resistant to or hostile towards progressive social changes and multiculturalism.")
    else:
        if (cult / 2) >= -15:
            print("You are Culturally Centre-Left")
            print("Culturally center-left refers to a perspective that supports progressive change and reforms in cultural norms and values while still valuing some degree of traditional practices.")
            print("This viewpoint generally advocates for inclusivity, diversity, and social justice, aiming to balance cultural evolution with respect for established traditions.")
        elif (cult / 2) > -30:
            if (cult / 2) < -15:
                print("You are Culturally Left-Wing")
                print("Culturally left refers to a perspective that promotes progressive changes in cultural norms and values, emphasizing inclusivity, diversity, and social justice.")
                print("This viewpoint often advocates for reforming or challenging traditional practices to address social inequalities and adapt to evolving cultural dynamics.")
        else:
            print("You are Culturally Far-Left")
            print("Culturally far-left refers to a viewpoint that seeks radical changes in cultural norms and values, aiming to fundamentally transform societal structures to promote equality and social justice.")
            print("This perspective often challenges and seeks to dismantle traditional institutions and practices perceived as oppressive or outdated, advocating for extensive cultural and social reform.")

    # Explaining their Economy axis
    print("\n-----ECONOMY-----")
    print(f"Your economic axis is {econ / 2}\n")
    if (econ / 2) > 0:
        if (econ / 2) <= 17:
            print("You are Economically Centre-Right")
            print("Economically center-right refers to a perspective that generally supports free-market principles, including limited government intervention in the economy, while still recognizing the need for some social safety nets and regulations.")
            print("This viewpoint favors fiscal responsibility, private enterprise, and policies that encourage economic growth, but with a moderate approach that balances market freedom with social stability.")
        elif (econ / 2) < 34:
            if (econ / 2) > 17:
                print("You are Economically Right-Wing")
                print("Economically right-wing refers to a perspective that strongly supports free-market capitalism, minimal government intervention, and the primacy of private enterprise.")
                print("This viewpoint emphasizes lower taxes, deregulation, and policies that favor individual economic freedom and entrepreneurship, often prioritizing economic growth over social welfare programs.")
        else:
             print("You are Economically Far-Right")
             print("Economically far-right refers to a perspective that advocates for extreme free-market capitalism with minimal to no government intervention in the economy.")
             print("This viewpoint typically promotes the privatization of most, if not all, public services, drastic reductions in taxes and regulations, and a strong emphasis on individual economic freedom, often at the expense of social welfare programs and collective economic responsibilities.")
    else:
        if (econ / 2) >= -17:
            print("Your Economically Centre-Left")
            print("Economically center-left refers to a perspective that supports a mixed economy, combining market-driven growth with a significant role for government intervention to promote social welfare and reduce inequality.")
            print("This viewpoint advocates for progressive taxation, public investment in essential services like healthcare and education, and regulations to ensure fair economic practices, while still valuing the benefits of a market economy.")
        elif (econ / 2) > -34:
            if (econ / 2) < -17:
                print("Your Economically Left-Wing")
                print("Economically left-wing refers to a perspective that advocates for a greater role of the government in managing the economy to promote social equity and reduce disparities.")
                print("This viewpoint supports policies such as higher taxation on the wealthy, extensive social welfare programs, public ownership or regulation of key industries, and a focus on redistributing wealth to achieve greater economic fairness.")
        else:
            print("Your Economically Far-Left")
            print("Economically far-left refers to a perspective that advocates for a radical restructuring of the economy, often favoring extensive government control or ownership of resources and industries.")
            print("This viewpoint typically supports policies aimed at eliminating economic inequality, such as wealth redistribution, the abolition of private property in favor of collective ownership, and the dismantling of capitalist structures in favor of a more egalitarian system.")

    # Explaining their Authority axis
    print("\n-----AUTHORITY-----")
    print(f"Your authority axis is {auth / 2}\n")
    if (auth / 2) > 0:
        if (auth / 2) <= 14:
            print("You are a Democratic Governmentalist...When it comes to the Government (This definition has no meaning whatsoever on your cultural and/or economic values)")
            print("A democratic governmentalist is someone who strongly supports the principles and structures of democratic governance, emphasizing the importance of democratic institutions, processes, and norms.")
            print("This viewpoint typically values the rule of law, representative elections, and the protection of individual rights and freedoms, advocating for the maintenance and strengthening of democratic systems as essential to fair and effective governance.")
        elif (auth / 2) < 35:
            if (auth / 2) > 14:
                print("You are an Authoritarian...When it comes to the Government (This definition has no meaning whatsoever on your cultural and/or economic values)")
                print("Authoritarianism is a political system characterized by concentrated power in a single authority or a small group, where political freedoms and democratic processes are highly restricted")
                print("In such systems, leaders often exert significant control over various aspects of life, including the media, judiciary, and civil society, limiting individual rights and dissent in favor of maintaining order and centralizing power.")
        else:
            print("You are a Totalitarian...When it comes to the Government (This definition has no meaning whatsoever on your cultural and/or economic values)")
            print("Totalitarianism is an extreme form of authoritarianism where the government seeks to control every aspect of public and private life, often through pervasive surveillance, propaganda, and repression.")
            print("In totalitarian regimes, the state exerts absolute authority over all institutions and sectors, aiming to create a uniform ideology and suppress any opposition or dissent, leaving no room for individual autonomy or alternative viewpoints.")
    else:
        if (auth / 2) >= -14:
            print("You are a Classical Liberal...When it comes to the Government (This definition has no meaning whatsoever on your cultural and/or economic values)")
            print("Classical liberalism is a political philosophy that emphasizes individual liberty, the protection of personal freedoms, and the rule of law.")
            print("It advocates for a limited government that safeguards these freedoms and ensures that power is derived from the consent of the governed, focusing on principles such as personal autonomy and equality before the law.")
        elif (auth / 2) > -28:
            if (auth / 2) < -14:
                print("You are a Libertarian...When it comes to the Government (This definition has no meaning whatsoever on your cultural and/or economic values)")
                print("Libertarianism is a political philosophy that prioritizes individual freedom and autonomy, advocating for minimal government intervention in personal and public affairs.")
                print("It emphasizes the protection of personal liberties and the belief that individuals should have the freedom to make their own choices as long as they do not infringe on the rights of others.")
        else:
            print("You are an Anarchist (Your economic and Cultural values discern what type you are)")
            print("Anarchism is a political philosophy that advocates for the abolition of hierarchical and coercive institutions, including the state.")
            print("It emphasizes the belief in self-governance and voluntary cooperation, proposing that society can function effectively without centralized authority or imposed rules.")

def main():
    culture_spectrum = axis_calc(culture_questions)
    economy_spectrum = axis_calc(economy_questions)
    authority_spectrum = axis_calc(authority_questions)

    explain(culture_spectrum, economy_spectrum, authority_spectrum)

main()
