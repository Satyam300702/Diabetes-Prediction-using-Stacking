# 🩸 Diabetes Prediction using Stacking Ensemble

## 🧠 Overview
This project is a **Machine Learning web application** that predicts whether a person is likely to have diabetes or not using a **Stacking Ensemble model**.

The model combines the power of **XGBoost**, **LightGBM**, and **CatBoost** as base learners, with **Naive Bayes** as the meta-learner, achieving a strong balance between **accuracy** and **generalization**.

The web interface is built using **Streamlit**, allowing users to input medical data and instantly get predictions.

---------------------------------------------------
## 🧬 Model Architecture

### 🔹 Base Models
- **XGBoostClassifier**
- **LightGBMClassifier**
- **CatBoostClassifier**

### 🔹 Meta Model
- **Gaussian Naive Bayes**
---------------------------------------------------
## 📈 Model Evaluation

| Metric | Score |
|---------|--------|
| **Test Accuracy** | 0.7338 |
| **ROC-AUC Score** | 0.8138 |

**Classification Report:**
| Class | Precision | Recall | F1-score |
|--------|------------|---------|-----------|
| 0 (Non-Diabetic) | 0.85 | 0.71 | 0.77 |
| 1 (Diabetic) | 0.60 | 0.78 | 0.68 |

**Confusion Matrix:**
[[70 29]
[12 43]]
---------------------------------------------------
Live Demo:-
---------------------------------------------------
GitHub Repo:- https://github.com/Satyam300702/Diabetes-Prediction-using-Stacking
---------------------------------------------------
Linkdlen :- www.linkedin.com/in/satyam-kumar-558269328
---------------------------------------------------
👨‍💻 Author

Satyam Kumar
📘 2nd Year CSE (AI & ML Engineering)