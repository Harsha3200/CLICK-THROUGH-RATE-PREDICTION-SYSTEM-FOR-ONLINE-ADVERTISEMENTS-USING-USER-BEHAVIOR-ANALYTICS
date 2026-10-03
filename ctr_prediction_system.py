"""
Click-Through Rate Prediction System
Predicts CTR using user behavior analytics and machine learning
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

def generate_ctr_dataset(n_samples=5000, random_state=42):
    """Generate synthetic CTR dataset"""
    np.random.seed(random_state)
    
    data = {
        'User_Age': np.random.randint(18, 75, n_samples),
        'User_Gender': np.random.choice(['M', 'F'], n_samples),
        'Device_Type': np.random.choice(['Mobile', 'Desktop', 'Tablet'], n_samples),
        'Ad_Category': np.random.choice(['Electronics', 'Fashion', 'Travel', 'Finance', 'Health'], n_samples),
        'Ad_Position': np.random.choice(['Top', 'Middle', 'Bottom', 'Sidebar'], n_samples),
        'Time_of_Day': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], n_samples),
        'Previous_Clicks': np.random.randint(0, 50, n_samples),
        'Session_Duration_Minutes': np.random.exponential(5, n_samples),
        'Page_Views': np.random.randint(1, 100, n_samples),
        'Ad_Relevance_Score': np.random.uniform(0, 1, n_samples),
        'User_Engagement_Score': np.random.uniform(0, 1, n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Create CTR based on features
    ctr_prob = (
        0.05 +
        (df['User_Age'] > 35) * 0.05 +
        (df['Device_Type'] == 'Mobile') * 0.08 +
        (df['Ad_Position'] == 'Top') * 0.1 +
        (df['Previous_Clicks'] > 10) * 0.08 +
        df['Ad_Relevance_Score'] * 0.15 +
        df['User_Engagement_Score'] * 0.12 +
        (df['Time_of_Day'] == 'Evening') * 0.06
    )
    
    df['Clicked'] = (np.random.rand(n_samples) < ctr_prob).astype(int)
    
    return df

def preprocess_data(df):
    """Preprocess CTR data"""
    df_processed = df.copy()
    
    # Encode categorical variables
    df_processed['Gender_Encoded'] = (df_processed['User_Gender'] == 'M').astype(int)
    df_processed['Device_Mobile'] = (df_processed['Device_Type'] == 'Mobile').astype(int)
    df_processed['Device_Desktop'] = (df_processed['Device_Type'] == 'Desktop').astype(int)
    df_processed['Ad_Top'] = (df_processed['Ad_Position'] == 'Top').astype(int)
    df_processed['Time_Evening'] = (df_processed['Time_of_Day'] == 'Evening').astype(int)
    
    # One-hot encode ad category
    ad_dummies = pd.get_dummies(df_processed['Ad_Category'], prefix='Category')
    df_processed = pd.concat([df_processed, ad_dummies], axis=1)
    
    # Select features
    feature_cols = [col for col in df_processed.columns if col not in 
                   ['User_Gender', 'Device_Type', 'Ad_Category', 'Ad_Position', 'Time_of_Day', 'Clicked']]
    
    return df_processed, feature_cols

def train_models(X_train, X_test, y_train, y_test):
    """Train multiple CTR prediction models"""
    models = {}
    results = []
    
    # Logistic Regression
    print("Training Logistic Regression...")
    lr = LogisticRegression(max_iter=1000, random_state=42)
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    y_proba_lr = lr.predict_proba(X_test)[:, 1]
    
    models['Logistic Regression'] = lr
    results.append({
        'Model': 'Logistic Regression',
        'Accuracy': accuracy_score(y_test, y_pred_lr),
        'Precision': precision_score(y_test, y_pred_lr, zero_division=0),
        'Recall': recall_score(y_test, y_pred_lr, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_lr, zero_division=0),
        'ROC-AUC': roc_auc_score(y_test, y_proba_lr)
    })
    
    # Random Forest
    print("Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    y_proba_rf = rf.predict_proba(X_test)[:, 1]
    
    models['Random Forest'] = rf
    results.append({
        'Model': 'Random Forest',
        'Accuracy': accuracy_score(y_test, y_pred_rf),
        'Precision': precision_score(y_test, y_pred_rf, zero_division=0),
        'Recall': recall_score(y_test, y_pred_rf, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_rf, zero_division=0),
        'ROC-AUC': roc_auc_score(y_test, y_proba_rf)
    })
    
    # Gradient Boosting
    print("Training Gradient Boosting...")
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb.fit(X_train, y_train)
    y_pred_gb = gb.predict(X_test)
    y_proba_gb = gb.predict_proba(X_test)[:, 1]
    
    models['Gradient Boosting'] = gb
    results.append({
        'Model': 'Gradient Boosting',
        'Accuracy': accuracy_score(y_test, y_pred_gb),
        'Precision': precision_score(y_test, y_pred_gb, zero_division=0),
        'Recall': recall_score(y_test, y_pred_gb, zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_gb, zero_division=0),
        'ROC-AUC': roc_auc_score(y_test, y_proba_gb)
    })
    
    return models, pd.DataFrame(results), y_pred_rf, y_proba_rf

def plot_ctr_distribution(df):
    """Plot CTR distribution"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    click_counts = df['Clicked'].value_counts()
    colors = ['#e74c3c', '#2ecc71']
    
    axes[0].bar(['No Click', 'Click'], click_counts.values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_ylabel('Count', fontsize=11, fontweight='bold')
    axes[0].set_title('Click Distribution in Dataset', fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(click_counts.values):
        axes[0].text(i, v + 50, str(v), ha='center', fontweight='bold')
    
    # CTR by device
    ctr_by_device = df.groupby('Device_Type')['Clicked'].agg(['sum', 'count'])
    ctr_by_device['CTR'] = (ctr_by_device['sum'] / ctr_by_device['count'] * 100).round(2)
    
    axes[1].bar(ctr_by_device.index, ctr_by_device['CTR'], color=['#3498db', '#e74c3c', '#2ecc71'], 
               alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_ylabel('CTR (%)', fontsize=11, fontweight='bold')
    axes[1].set_title('CTR by Device Type', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(ctr_by_device['CTR']):
        axes[1].text(i, v + 0.5, f'{v:.2f}%', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_distribution.png")
    plt.close()

def plot_model_comparison(results_df):
    """Plot model performance comparison"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
    x = np.arange(len(results_df))
    width = 0.15
    
    for idx, metric in enumerate(metrics):
        axes[0].bar(x + idx * width, results_df[metric], width, label=metric, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    axes[0].set_xlabel('Model', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Score', fontsize=11, fontweight='bold')
    axes[0].set_title('Model Performance Comparison', fontsize=12, fontweight='bold')
    axes[0].set_xticks(x + width * 2)
    axes[0].set_xticklabels(results_df['Model'], fontsize=10)
    axes[0].legend(fontsize=9, loc='lower right')
    axes[0].grid(axis='y', alpha=0.3)
    axes[0].set_ylim([0, 1.1])
    
    # ROC-AUC comparison
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    axes[1].bar(results_df['Model'], results_df['ROC-AUC'], color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_ylabel('ROC-AUC Score', fontsize=11, fontweight='bold')
    axes[1].set_title('Model ROC-AUC Comparison', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    axes[1].set_ylim([0, 1.1])
    
    for i, v in enumerate(results_df['ROC-AUC']):
        axes[1].text(i, v + 0.02, f'{v:.3f}', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_model_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_model_comparison.png")
    plt.close()

def plot_confusion_matrices(models, X_test, y_test):
    """Plot confusion matrices"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    for idx, (model_name, model) in enumerate(models.items()):
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                   xticklabels=['No Click', 'Click'], yticklabels=['No Click', 'Click'],
                   cbar=False, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
        axes[idx].set_title(f'{model_name}', fontsize=12, fontweight='bold')
        axes[idx].set_ylabel('True Label', fontsize=10, fontweight='bold')
        axes[idx].set_xlabel('Predicted Label', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_confusion_matrices.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_confusion_matrices.png")
    plt.close()

def plot_roc_curves(models, X_test, y_test):
    """Plot ROC curves"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    
    for idx, (model_name, model) in enumerate(models.items()):
        y_proba = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_proba)
        auc = roc_auc_score(y_test, y_proba)
        
        ax.plot(fpr, tpr, color=colors[idx], lw=2, label=f'{model_name} (AUC = {auc:.3f})', marker='o', markersize=4)
    
    ax.plot([0, 1], [0, 1], 'k--', lw=2, label='Random Classifier')
    ax.set_xlabel('False Positive Rate', fontsize=11, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=11, fontweight='bold')
    ax.set_title('ROC Curves - CTR Prediction', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_roc_curves.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_roc_curves.png")
    plt.close()

def plot_feature_importance(models):
    """Plot feature importance"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Random Forest
    rf = models['Random Forest']
    feature_importance_rf = pd.DataFrame({
        'Feature': range(len(rf.feature_importances_)),
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False).head(10)
    
    axes[0].barh(feature_importance_rf['Feature'].astype(str), feature_importance_rf['Importance'], 
                color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[0].set_title('Random Forest - Top 10 Features', fontsize=12, fontweight='bold')
    axes[0].invert_yaxis()
    axes[0].grid(axis='x', alpha=0.3)
    
    # Gradient Boosting
    gb = models['Gradient Boosting']
    feature_importance_gb = pd.DataFrame({
        'Feature': range(len(gb.feature_importances_)),
        'Importance': gb.feature_importances_
    }).sort_values('Importance', ascending=False).head(10)
    
    axes[1].barh(feature_importance_gb['Feature'].astype(str), feature_importance_gb['Importance'],
                color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1].set_xlabel('Importance', fontsize=11, fontweight='bold')
    axes[1].set_title('Gradient Boosting - Top 10 Features', fontsize=12, fontweight='bold')
    axes[1].invert_yaxis()
    axes[1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_feature_importance.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_feature_importance.png")
    plt.close()

def plot_ctr_by_features(df):
    """Plot CTR by different features"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # CTR by age group
    df['Age_Group'] = pd.cut(df['User_Age'], bins=[0, 25, 35, 50, 75], labels=['18-25', '26-35', '36-50', '50+'])
    ctr_age = df.groupby('Age_Group')['Clicked'].agg(['sum', 'count'])
    ctr_age['CTR'] = (ctr_age['sum'] / ctr_age['count'] * 100).round(2)
    
    axes[0, 0].bar(ctr_age.index.astype(str), ctr_age['CTR'], color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0, 0].set_ylabel('CTR (%)', fontsize=10, fontweight='bold')
    axes[0, 0].set_title('CTR by Age Group', fontsize=11, fontweight='bold')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # CTR by ad category
    ctr_category = df.groupby('Ad_Category')['Clicked'].agg(['sum', 'count'])
    ctr_category['CTR'] = (ctr_category['sum'] / ctr_category['count'] * 100).round(2)
    
    axes[0, 1].bar(ctr_category.index, ctr_category['CTR'], color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[0, 1].set_ylabel('CTR (%)', fontsize=10, fontweight='bold')
    axes[0, 1].set_title('CTR by Ad Category', fontsize=11, fontweight='bold')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # CTR by ad position
    ctr_position = df.groupby('Ad_Position')['Clicked'].agg(['sum', 'count'])
    ctr_position['CTR'] = (ctr_position['sum'] / ctr_position['count'] * 100).round(2)
    
    axes[1, 0].bar(ctr_position.index, ctr_position['CTR'], color='#2ecc71', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1, 0].set_ylabel('CTR (%)', fontsize=10, fontweight='bold')
    axes[1, 0].set_title('CTR by Ad Position', fontsize=11, fontweight='bold')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # CTR by time of day
    ctr_time = df.groupby('Time_of_Day')['Clicked'].agg(['sum', 'count'])
    ctr_time['CTR'] = (ctr_time['sum'] / ctr_time['count'] * 100).round(2)
    
    axes[1, 1].bar(ctr_time.index, ctr_time['CTR'], color='#f39c12', alpha=0.8, edgecolor='black', linewidth=1.5)
    axes[1, 1].set_ylabel('CTR (%)', fontsize=10, fontweight='bold')
    axes[1, 1].set_title('CTR by Time of Day', fontsize=11, fontweight='bold')
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/ctr_by_features.png', dpi=300, bbox_inches='tight')
    print("Saved: ctr_by_features.png")
    plt.close()

def main():
    print("="*80)
    print("CLICK-THROUGH RATE PREDICTION SYSTEM - USER BEHAVIOR ANALYTICS")
    print("="*80)
    
    # Generate dataset
    print("\n[1] Generating synthetic CTR dataset...")
    df = generate_ctr_dataset(n_samples=5000)
    df.to_csv('/home/ubuntu/ctr_data.csv', index=False)
    print(f"Dataset generated: {len(df)} records")
    print(f"Click rate: {df['Clicked'].mean()*100:.2f}%")
    
    # Preprocess data
    print("\n[2] Preprocessing data...")
    df_processed, feature_cols = preprocess_data(df)
    X = df_processed[feature_cols].values
    y = df_processed['Clicked'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set: {len(X_train)}, Test set: {len(X_test)}")
    
    # Train models
    print("\n[3] Training CTR prediction models...")
    models, results_df, y_pred_rf, y_proba_rf = train_models(X_train, X_test, y_train, y_test)
    results_df.to_csv('/home/ubuntu/ctr_model_results.csv', index=False)
    print("\nModel Results:")
    print(results_df.to_string(index=False))
    
    # Generate visualizations
    print("\n[4] Generating visualizations...")
    plot_ctr_distribution(df)
    plot_model_comparison(results_df)
    plot_confusion_matrices(models, X_test, y_test)
    plot_roc_curves(models, X_test, y_test)
    plot_feature_importance(models)
    plot_ctr_by_features(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE - All visualizations saved")
    print("="*80)

if __name__ == "__main__":
    main()
