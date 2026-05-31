import json
import pandas as pd

json_file_name = "user_data_tiktok.json"  # Nhớ đổi tên đúng file của bạn nhé


def convert_tiktok_json():
    try:
        # 1. Đọc file JSON
        with open(json_file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("🔄 Đang bóc tách và chuyển đổi dữ liệu...")

        # --- PHẦN 1: TRÍCH XUẤT VIDEO ĐÃ ĐĂNG (POSTS) ---
        try:
            posts_data = data["Post"]["Posts"]["VideoList"]
            df_posts = pd.DataFrame(posts_data)

            # Xuất ra file CSV cho Video đã đăng
            posts_csv = "tiktok_my_posts.csv"
            df_posts.to_csv(posts_csv, index=False, encoding="utf-8-sig")
            print(f"✅ Đã xuất file video đã đăng: '{posts_csv}' ({len(df_posts)} videos)")
        except KeyError:
            print("⚠️ Không tìm thấy dữ liệu Video đã đăng (Post) trong file.")

        # --- PHẦN 2: TRÍCH XUẤT VIDEO ĐÃ THÍCH/LƯU (FAVORITES) ---
        try:
            fav_data = data["Likes and Favorites"]["Favorite Videos"][
                "FavoriteVideoList"
            ]
            df_favs = pd.DataFrame(fav_data)

            # Xuất ra file CSV cho Video yêu thích
            favs_csv = "tiktok_favorite_videos.csv"
            df_favs.to_csv(favs_csv, index=False, encoding="utf-8-sig")
            print(f"✅ Đã xuất file video yêu thích: '{favs_csv}' ({len(df_favs)} videos)")
        except KeyError:
            print(
                "⚠️ Không tìm thấy dữ liệu Video yêu thích (Favorite Videos) trong file."
            )

        print("\n🎉 Hoàn thành! Bây giờ bạn đã có các file CSV sạch để phân tích.")

    except Exception as e:
        print(f"❌ Lỗi hệ thống: {e}")


if __name__ == "__main__":
    convert_tiktok_json()