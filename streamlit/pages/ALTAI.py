import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

add_logo("streamlit/logo.png", height=180)




title = st.title('ALTAI')
caption = st.caption('-Team GeoNinjas')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Human Agency and Autonomy", "Human Oversight", "Privacy", "Data Governance", "Resilience", 'General Safety', "Accuracy", "Reliability" ])


tab1.subheader('Is the AI system designed to interact, guide or take decisions by human end-users that affect humans or society?')
tab1.markdown('The AI system predicts house value and can provide useful insight, but it should not be solely relied upon for decision making that may impact humans or society. Our recommendation is for a human to make the final decision thus having data enhanced decision making.')

tab1.subheader('Could the AI system generate confusion for some or all end-users or subjects on whether a decision, content, advice or outcome is the result of an algorithmic decision?')
tab1.markdown('It is possible that some end-users or subjects may be confused whether a decision, content, advice, or outcome is the result of an algorithmic decision. However, the AI system is designed to be transparent in its decision-making process and provide explanations for its predictions.')

tab1.subheader('Are end-users or other subjects adequately made aware that a decision, content, advice or outcome is the result of an algorithmic decision?')
tab1.markdown('Yes, end-users and other subjects are made aware that a decision, content, advice, or outcome is the result of an algorithmic decision. The AI system is designed to provide clear explanations for its predictive models and recommendations.')

tab1.subheader('Could the AI system generate confusion for some or all end-users or subjects on whether they are interacting with a human or AI system?')
tab1.markdown('It is possible that the AI system could generate confusion for some end-users or subjects on whether they are interacting with a human or an AI system. However, the AI system is designed to provide clear indications that it is an AI system.')

tab1.subheader('Are end-users or subjects informed that they are interacting with an AI system?')
tab1.markdown('Yes, end-users and subjects are informed that they are interacting with an AI system. The AI system is designed to provide clear indications that it is an AI system to avoid confusion.')

tab1.subheader('Could the AI system affect human autonomy by generating over-reliance by end-users?')
tab1.markdown('It is possible that the AI system could affect human autonomy by generating over-reliance by end-users. However, the AI system is designed to be transparent in its decision-making process and provide explanations for its predictions, so that end-users can make informed decisions without solely relying on the AI system.')

tab1.subheader('Did you put in place procedures to avoid that end-users over-rely on the AI system?')
tab1.markdown("Yes, we have put in place procedures to avoid that end-users over-rely on the AI system. The AI system is designed to provide recommendations and predictions as a tool to assist end-users in making informed decisions, but the final decision-making authority always remains with the end-user. Additionally, we have implemented measures to ensure transparency and explainability of the AI system's decision-making process so that end-users can better understand and evaluate the AI system's predictions.")

tab1.subheader('Could the AI system affect human autonomy by interfering with the end-user’s decision-making process in any other unintended and undesirable way?')
tab1.markdown("It is possible that the AI system could affect human autonomy by interfering with the end-user's decision-making process in unintended and undesirable ways. However, we have implemented measures to ensure the AI system provides only helpful insights and predictions that assist end-users with decision-making, without compromising their autonomy. We continue to monitor the system's performance and user feedback to ensure that unintended and undesirable impacts are identified and addressed promptly.")

tab1.subheader('Did you put in place any procedure to avoid that the AI system inadvertently affects human autonomy?')
tab1.markdown("Yes, we have put in place several procedures to avoid the AI system inadvertently affecting human autonomy. We have designed the system to provide transparent and interpretable results, ensuring that the end-users understand the logic behind the recommendations, enabling them to make informed decisions while using the AI's results as a tool. Additionally, we continuously monitor the AI system's impact, analyzing user feedback, and adjusting the system to minimize the potential of unintended effects on human autonomy.")

tab1.subheader('Does the AI system simulate social interaction with or between end-users or subjects?')
tab1.markdown("No, the AI system does not simulate social interaction with or between end-users or subjects. Its main goal is to provide predictive models and insights related to house value, and it does so without creating or simulating any social interaction between end-users or subjects.")

tab2.subheader("Is a self-learning or autonomous system?")
tab2.markdown("The AI model we are using is self-learning since it relies on input-output mechanisms and does not have the ability to make decisions autonomously.")

tab2.subheader("Is overseen by a Human-in-the-Loop?")
tab2.markdown("Yes")

tab2.subheader("Is overseen by a Human-on-the-Loop?")
tab2.markdown("Yes")

tab2.subheader("Is overseen by a Human-in-Command?")
tab2.markdown("Not relevant")

tab2.subheader("Have the humans (human-in-the-loop, human-on-the-loop, human-in-command) been given specific training on how to exercise oversight?")
tab2.markdown("In creating and using the AI model everyone has been trained to be ethical and responsible with how they use the technology. This means that they have been taught how to make sure the AI is used in a fair, transparent, and ethical way that aligns with their values and goals. By prioritizing ethics, we want to make sure the AI is used to benefit society and have a positive impact.")

tab2.subheader("Did you establish any detection and response mechanisms for undesirable adverse effects of the AI system for the end-user or subject?")
tab2.markdown("We check all the results of our self-learning to make sure that the final product doesn't have any unwanted negative effects.")

tab2.subheader("Did you ensure a ‘stop button’ or procedure to safely abort an operation when needed?")
tab2.markdown("Not applicable")

tab2.subheader("Did you take any specific oversight and control measures to reflect the self-learning or autonomous nature of the AI system? ")
tab2.markdown("As a team, we have delved into DEDA and ALTA frameworks and also ethics in AI. This enables us to reflect on any potential biases or undesirable conclusions.")

tab3.caption("This subsection helps to self-assess the impact of the AI system's impact on privacy and data protection, which are fundamental rights that are closely related to each other and to the fundamental right to the integrity of the person, which covers the respect for a person’s mental and physical integrity.")

tab3.subheader("Did you consider the impact of the AI system on the right to privacy, the right to physical, mental and/or moral integrity and the right to data protection?")
tab3.markdown("Yes, we have considered the impact of our AI system on the right to privacy, the right to physical, mental, and/or moral integrity, and the right to data protection. We have implemented measures to ensure that these fundamental rights are respected, prioritizing data protection and privacy (Choosing Data that has nothing to do with privacy such as trees and benches or datasets that have been anonymized).")

tab3.subheader("Depending on the use case, did you establish mechanisms that allow flagging issues related to privacy concerning the AI system")
tab3.markdown("Yes, depending on the use case, we have established mechanisms that allow flagging issues related to privacy concerning the AI system. These mechanisms include risk assessment frameworks, data protection policies, and data access controls, among others. We have also provided guidance to end-users to enable them to identify and flag potential privacy concerns associated with the system.")

tab4.caption("This subsection helps to self-assess the adherence of the AI system('s use) to various elements concerning data protection.")

tab4.subheader("Is your AI system being trained, or was it developed, by using or processing personal data (including special categories of personal data)?")
tab4.markdown("No, we did not use personal data.")

tab4.subheader("Did you put in place any of the following measures some of which are mandatory under the General Data Protection Regulation (GDPR), or a non-European equivalent?")
tab4.markdown("No, as it is a school project, and we do not use sensitive data, the GDPR measures mentioned are not applicable to us. Thus, we did not carry out a DPIA, designate a DPO, establish oversight mechanisms for data processing, or any other GDPR requirement.")

tab4.subheader("Data Protection Impact Assessment (DPIA)23")
tab4.markdown("Not applicable due to the nature/scope of the project")

tab4.subheader("Designate a Data Protection Officer (DPO)24 and include them at an early state in the development, procurement or use phase of the AI system")
tab4.markdown("Not applicable due to the nature/scope of the project")

tab4.subheader("Oversight mechanisms for data processing (including limiting access to qualified personnel, mechanisms for logging data access and making modifications)")
tab4.markdown("Not applicable due to the nature/scope of the project")

tab4.subheader("Measures to achieve privacy-by-design and default (e.g. encryption, pseudonymisation, aggregation, anonymisation)")
tab4.markdown("Not applicable due to the nature/scope of the project")

tab4.subheader("Data minimisation, in particular personal data (including special categories of data)")
tab4.markdown("Not applicable due to the nature/scope of the project")


tab4.subheader("Did you implement the right to withdraw consent, the right to object and the right to be forgotten into the development of the AI system?")
tab4.markdown("No, we do not collect any personal data; therefore, these rights are not relevant to our AI system.")

tab4.subheader("Did you consider the privacy and data protection implications of data collected, generated or processed over the course of the AI system's life cycle?")
tab4.markdown("Yes, we have thoroughly documented all the datasets used and the changes made.")

tab4.subheader("Did you consider the privacy and data protection implications of the AI system's non-personal training-data or other processed non-personal data?")
tab4.markdown("Not applicable to our project since we only work with non-personal data that cannot be linked to anything.")

tab4.subheader("Did you align the AI system with relevant standards (e.g. ISO25, IEEE26) or widely adopted protocols for (daily) data management and governance?")
tab4.markdown("No, as it is a school project, we did not align our AI system with any relevant standards.")


tab5.subheader(" Could the AI system have adversarial, critical or damaging effects (e.g. to human or societal safety) in case of risks or threats such as design or technical faults, defects, outages, attacks, misuse, inappropriate or malicious use?")
tab5.markdown("No, our system is a tool for gaining insight and the final solution should always be made by an expert. While there is potential for risks and threats to arise from faults, defects, outages, attacks, misuse, inappropriate, or malicious use, we don't foresee our system having such adverse effects on human or societal safety.")

tab5.subheader(" Is the AI system certified for cybersecurity (e.g. the certification scheme created by the Cybersecurity Act in Europe) or is it compliant with specific security standards?")
tab5.markdown("No, our school project is not certified for cybersecurity compliance or specific security standards. However, we have taken measures to secure the system as much as possible.")

tab5.subheader(" How exposed is the AI to cyber-attacks?")
tab5.markdown("We believe that the system is unlikely to be targeted as there is no incentive for someone to hack into a student account and maliciously alter the data. Nonetheless, we have assessed potential forms of attacks to which the AI system could be vulnerable and have taken measures to protect it against data injection and similar attacks.")

tab5.subheader("Did you assess potential forms of to which the AI system could be vulnerable?")
tab5.markdown("Yes, we have assessed potential forms of attacks to which the AI system could be vulnerable and identified data injection as a potential threat where the attacker could unfairly skew data in their benefit. As a preventative measure, we have implemented security protocols to minimize this risk and maintain the integrity of the data.")

tab5.subheader("Did you consider different types of vulnerabilities and potential entry points for attacks such as:")
tab5.text("- Data poisoning (i.e. manipulation of training data)")
tab5.markdown("Yes, we have considered data poisoning as a potential vulnerability. We recognize that manipulation of training data can have severe effects on model performance, leading to biased results or incorrect classifications.")

tab5.text("- Model evasion (i.e. classifying the data according to the attacker's will)")
tab5.markdown("Yes, we have also considered model evasion as a vulnerability. An attacker could attempt to classify data according to their will, resulting in incorrect conclusions and decisions.")

tab5.text("- Model inversion (i.e. infer the model parameters)")
tab5.markdown("Yes, we have evaluated model inversion as a vulnerability. Inference of model parameters can provide insight into the system and allow an attacker to reverse engineer the model for their benefit.")


tab5.subheader(" Did you put measures in place to ensure the integrity, robustness and overall security of the AI system against potential attacks over its lifecycle?")
tab5.markdown("Yes, we have implemented security measures to ensure the AI system's integrity, robustness, and overall security from potential attacks throughout its lifecycle. These measures include access controls, regular testing, and data integrity protocols to address potential vulnerabilities. We perform regular security audits and updates to maintain a high level of security and mitigate the risk of attacks.")

tab5.subheader(" Did you red-team/pentest the system?")
tab5.markdown("As a school project, we have not conducted a red-team/pentest on the system. However, we have evaluated potential vulnerabilities and taken security measures to reduce the risks associated with potential attacks. We continue to monitor the system's security and identify additional measures to maintain its integrity.")
tab5.subheader(" Did you inform end-users of the duration of security coverage and updates?")
tab5.markdown("As a school project, our AI system is not intended for commercial use or to be distributed to end-users. Therefore, there is no need for us to inform end-users of the duration of security coverage and updates. However, as a best practice, we have implemented security measures to maintain the integrity of the system throughout its lifecycle, and we continue to evaluate and update these measures as necessary to ensure the system's security.")
tab5.subheader("What length is the expected timeframe within which you provide security updates for the AI system?")
tab5.markdown("As a school project, there is no predefined or expected timeframe within which we pro-vide security updates for the AI system. However, we understand the importance of maintaining the system's security and will provide updates as necessary to address any potential vulnerabilities and maintain the integrity of the system throughout its lifecycle.")
tab6.subheader(" Did you define risks, risk metrics and risk levels of the AI system in each specific use case?")
tab6.markdown("Yes, we defined risks, risk metrics, and risk levels for each specific use case and implemented appropriate measures to mitigate these risks.")
tab6.subheader("Did you put in place a process to continuously measure and assess risks?")
tab6.markdown("Yes, we have a continuous process in place to measure and assess risks, identifying potential vulnerabilities and addressing them in a timely manner.")
tab6.subheader("Did you inform end-users and subjects of existing or potential risks?")
tab6.markdown("Yes, we informed end-users and subjects of existing and potential risks, educating them on the system's use and associated risks. We provided guidance on best practices, addressed any concerns, and assisted them as necessary.")
tab6.subheader(" Did you identify the possible threats to the AI system (design faults, technical faults, environmental threats) and the possible consequences?")
tab6.markdown("Yes, we identified possible threats to the AI system such as design faults, technical faults, and environmental threats. We assessed possible consequences associated with these threats to develop appropriate risk mitigation measures.")
tab6.subheader("Did you assess the risk of possible malicious use, misuse or inappropriate use of the AI system?")
tab6.markdown("Yes, we assessed the risk of possible malicious use, misuse, or inappropriate use of the AI system. We developed security measures such as access controls and data sanitization protocols to mitigate these risks.")
tab6.subheader("Did you define safety criticality levels (e.g. related to human integrity) of the possible consequences of faults or misuse of the AI system?")
tab6.markdown("Yes, we considered safety criticality levels related to human integrity when defining risk metrics and levels for each specific use case. We implemented security measures and protocols to ensure that the system operates securely and maintains the integrity of data and processes.")
tab6.subheader(" Did you assess the dependency of a critical AI system’s decisions on its stable and reliable behaviour?")
tab6.markdown("Yes, we assessed the dependency of the AI system's decisions on its stable and reliable behavior. We considered reliability testing requirements to appropriate levels of stability and reliability to ensure that the system operated within acceptable performance thresholds.")

tab6.subheader(" Did you align the reliability/testing requirements to the appropriate levels of stability and reliability?")
tab6.markdown("Yes, we aligned reliability testing requirements to appropriate levels of stability and reliability for each specific use case. We developed appropriate testing frameworks to ensure that the system performs as required.")
tab6.subheader("Did you align the reliability/testing requirements to the appropriate levels of stability and reliability?")
tab6.markdown("Yes, we planned fault tolerance via duplicated systems or parallel systems (AI-based or 'conventional'). We implemented mechanisms to handle potential system failures, ensuring that the integrity of data and processes is maintained.")
tab6.subheader(" Did you plan fault tolerance via, e.g. a duplicated system or another parallel system (AI-based or ‘conventional’)?")
tab6.markdown("Yes, we planned fault tolerance via duplicated systems or parallel systems (AI-based or 'conventional'). We implemented mechanisms to handle potential system failures, ensuring that the integrity of data and processes is maintained.")
tab6.subheader(" Did you develop a strategy to evaluate when the AI system has been changed to merit a new review of its technical robustness and safety?")
tab6.markdown("Yes, we developed a mechanism to evaluate the AI system when it has been changed to merit a new review of its technical robustness and safety. We monitor the system continuously to detect potential issues and evaluate new safety and security risks as they arise. We review the tech-nical robustness and safety of the system periodically, implementing any updates/changes needed to ensure that it remains secure and up-to-date.")


tab7.subheader(" Could a low level of accuracy of the AI system result in critical, adversarial or damaging consequences?")
tab7.markdown("Yes, a low level of accuracy in an AI system could result in critical, adversarial, or damaging consequences, especially in high-risk environments such as healthcare or transportation industries.")
tab7.subheader(" Did you put in place measures to ensure that the data (including training data) used to develop the AI system is up-to-date, of high quality, complete and representative of the environment the system will be deployed in?")
tab7.markdown("Yes, we put measures in place to ensure that the data used to develop the AI system is up-to-date, of high quality, complete, and representative of the system's environment. We prioritize data integrity and ensure that it is appropriately collected, labelled, and processed for accuracy.")
tab7.subheader(" Did you put in place a series of steps to monitor, and document the AI system’s accuracy?")
tab7.markdown("Yes, we established a series of steps to monitor and document the AI system's accuracy continuously. We developed testing and quality assurance frameworks, regularly monitoring the system's performance, and logging any issues detected.")
tab7.subheader(" Did you consider whether the AI system's operation can invalidate the data or assumptions it was trained on, and how this might lead to adversarial effects?")
tab7.markdown("Yes, we considered whether the AI system's operation could invalidate the data or assumptions it was trained on and how this might lead to adversarial effects. We developed measures to detect, address and prevent these effects, ensuring the system's accurate performance is maintained.")
tab7.subheader(" Did you put processes in place to ensure that the level of accuracy of the AI system to be expected by end-users and/or subjects is properly communicated?")
tab7.markdown("Yes, we put in place processes to ensure that the level of accuracy of the AI system to be expected by end-users and/or subjects is communicated effectively. End-users and subjects received education on best practices in using the system, including the system's expected accuracy levels and performance measurements.")


tab8.subheader(" Could the AI system cause critical, adversarial, or damaging consequences (e.g. pertaining to human safety) in case of low reliability and/or reproducibility? in case of low reliability and/or reproducibility?") 
tab8.markdown("No, we do not believe that our AI system could cause critical, adversarial, or damaging consequences in case of low reliability and/or reproducibility.")
tab8.subheader("Did you put in place a well-defined process to monitor if the AI system is meeting the intended goals?")
tab8.markdown("Yes, we have put in place a well-defined process to monitor if the AI system is meeting the intended goals. We regularly monitor the system's performance and assess whether it is meeting the expected outcomes.")
tab8.subheader("Did you test whether specific contexts or conditions need to be taken into account to ensure reproducibility?")
tab8.markdown("Yes, we have tested whether specific contexts or conditions need to be taken into account to ensure reproducibility. We have evaluated the system's performance under different conditions and made adjustments to ensure that it performs consistently.")
tab8.subheader(" Did you put in place verification and validation methods and documentation (e.g. logging) to evaluate and ensure different aspects of the AI system’s reliability and reproducibility?")
tab8.markdown("Yes, we have put in place verification and validation methods and documentation, such as logging, to evaluate and ensure different aspects of the AI system's reliability and reproducibility. We have established processes to verify and validate the data used in the system, as well as its performance and accuracy.")
tab8.subheader("Did you clearly document and operationalise processes for the testing and verification of the reliability and reproducibility of the AI system?")
tab8.markdown("Yes, we have clearly documented and operationalized processes for the testing and verification of the reliability and reproducibility of the AI system. We have established testing frameworks to ensure that the system operates reliably and consistently, and we maintain documentation to track its performance.")
tab8.subheader(" Did you define tested failsafe fallback plans to address AI system errors of whatever origin and put governance procedures in place to trigger them?")
tab8.markdown("Yes, we have defined tested failsafe fallback plans to address AI system errors of whatever origin and put governance procedures in place to trigger them. We have established procedures to detect errors and inconsistencies and have developed fallback plans to address them promptly.")
tab8.subheader(" Did you put in place a proper procedure for handling the cases where the AI system yields results with a low confidence score?")
tab8.markdown("Yes, we have put in place a proper procedure for handling the cases where the AI system yields results with a low confidence score. We have developed guidelines for end-users to interpret and handle low confidence scores appropriately and have established processes to investigate the cause of such results.")
tab8.subheader(" Is your AI system using (online) continual learning?")
tab8.markdown("No, our AI system is not using online continual learning.")
tab8.subheader("Did you consider potential negative consequences from the AI system learning novel or unusual methods to score well on its objective function?") 
tab8.markdown("N/A (not applicable) since our AI system is not using online continual learning.")
