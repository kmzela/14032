import json

def save_results_to_json(results, filename='results.json'):
    """ذخیره نتایج در فایل JSON."""
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def my_final_grade_calculation(filename):
    """محاسبه نمرات نهایی و تعیین وضعیت قبولی یا ناموفقی."""
    results = {}
    
    with open(filename, 'r') as file:
        for line in file:
            # تقسیم خط به بخش‌های مختلف
            data = line.strip().split(',')
            name = data[0].strip().lower()  # تبدیل نام به حروف کوچک
            
            # تبدیل نمرات به اعداد صحیح
            scores = list(map(int, [score.strip() for score in data[1:]]))

            # بررسی تعداد نمرات
            if len(scores) != 12:
                raise ValueError(f"Invalid number of scores for {name}: {len(scores)} found, but 12 expected.")

            # محاسبه میانگین نمرات آزمون‌ها
            quizzes = sorted(scores[0:6])
            quizzes_avg = (sum(quizzes[2:]) / 4) * 0.25  # میانگین چهار نمره باقی‌مانده
            
            # محاسبه میانگین نمرات تکالیف
            assignments = sorted(scores[6:10])
            assignments_avg = (sum(assignments[1:]) / 3) * 0.25  # میانگین سه نمره باقی‌مانده
            
            # محاسبه نمره میان ترم و نهایی
            midterm_weight = scores[10] * 0.25
            final_weight = scores[11] * 0.25

            # محاسبه نمره نهایی
            final_score = quizzes_avg + assignments_avg + midterm_weight + final_weight
            
            # بررسی قبولی یا ناموفقی
            status = 'pass' if final_score >= 60 else 'fail'
            results[name] = status  # ذخیره وضعیت
        
    # ذخیره نتایج در فایل JSON
    save_results_to_json(results)

    return results

# استفاده از تابع
filename = 'grades.txt'  # نام فایل ورودی
grades_result = my_final_grade_calculation(filename)
print(grades_result)