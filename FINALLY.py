import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def get_next_folder_number(base_folder='kano_results'):
    """
    Функция для получения следующего доступного номера папки для сохранения результатов.
    Проверяет существующие папки и находит максимальный номер.

    :param base_folder: Имя базовой папки.
    :return: Следующий доступный номер папки.
    """
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)  # Создаем базовую папку, если она не существует
        return 1  # Если папок не было, возвращаем первый номер

    existing_folders = [int(d) for d in os.listdir(base_folder) if d.isdigit()]
    return max(existing_folders, default=0) + 1  # Возвращаем следующий номер

def categorize_kano_and_plot(innovations):
    """
    Функция для классификации нововведений по категориям Кано на основе оценок пользователей
    и отображения их на координатной плоскости.

    :param innovations: Словарь с нововведениями, где ключом является название нововведения,
                        а значением - список оценок пользователей.
    :return: Словарь с нововведениями, их средней оценкой и категорией Кано.
    """

    results = []

    for innovation, ratings in innovations.items():
        average_rating = sum(ratings) / len(ratings)
        average_rating = round(average_rating, 2)  # Округляем до 2 знаков после запятой

        # Определяем категорию Кано
        if average_rating < 3:
            category = "Базовое"
        elif 3 <= average_rating < 4:
            category = "Ожидаемое"
        elif 4 <= average_rating <= 5:
            category = "Привлекательное"
        else:
            category = "Необязательное"  # В случае, если оценки выходят за пределы 1-5

        results.append({
            "Нововведение": innovation,
            "Средняя оценка": average_rating,
            "Категория Кано": category,
            "Количество голосов": len(ratings)
        })

    # Преобразуем результаты в DataFrame
    df = pd.DataFrame(results)

    # Получаем следующий номер папки
    folder_number = get_next_folder_number()
    folder_name = os.path.join('kano_results', str(folder_number))  # Формируем имя папки
    os.makedirs(folder_name, exist_ok=True)  # Создаем папку

    # Сохраняем результаты в CSV файл с разделителем ';'
    output_file = os.path.join(folder_name, 'kano_results.csv')
    df.to_csv(output_file, sep=';', index=False)

    # Визуализация с использованием Seaborn
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Средняя оценка", y="Количество голосов", hue="Категория Кано", style="Категория Кано", s=100)

    # Добавляем подписи для точек
    for i in range(df.shape[0]):
        plt.text(df["Средняя оценка"].iloc[i], df["Количество голосов"].iloc[i],
                 df["Нововведение"].iloc[i], horizontalalignment='left', size='medium', color='black')

    plt.axvline(x=3, color='r', linestyle='--', label='Граница для базовых/ожидаемых')
    plt.axvline(x=4, color='g', linestyle='--', label='Граница для ожидаемых/привлекательных')

    plt.title("Классификация нововведений по категориям Кано")
    plt.xlabel("Средняя оценка")
    plt.ylabel("Количество голосов")
    plt.legend(title="Категория Кано", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    plt.tight_layout()

    # Сохраняем график как изображение
    plot_file = os.path.join(folder_name, 'kano_plot.png')
    plt.savefig(plot_file)
    plt.close()  # Закрываем фигуру после сохранения

    print(f"Результаты сохранены в {output_file}")
    print(f"График сохранен в {plot_file}")

    # Добавляем ссылку на изображение в результирующий DataFrame
    df['Ссылка на график'] = plot_file

    return results

# Пример данных
innovations_data = {
    "Нововведение 1": [5, 4, 5, 4, 5, 2, 2],
    "Нововведение 2": [2, 2, 3],
    "Нововведение 3": [5, 5, 5, 5],
    "Нововведение 4": [2, 2, 2, 2, 2, 2]
}

# Вызываем функцию
kano_results = categorize_kano_and_plot(innovations_data)

# Печатаем результаты
for result in kano_results:
    print(f"{result['Нововведение']}: Средняя оценка = {result['Средняя оценка']:.2f}, Категория = {result['Категория Кано']}, Количество голосов = {result['Количество голосов']}")
