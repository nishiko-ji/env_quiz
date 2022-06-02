import pyqrcode as qr
import cv2
import numpy as np


def create_qrcode(filename, string):
    qr.create(string, error='L', version=3, mode='binary').png(
        filename,
        scale=5,
        module_color=[0, 0, 0, 128],
        background=[255, 255, 255]
        )


def qrdec_cv2(img_bgr):
    font = cv2.FONT_HERSHEY_SIMPLEX

    # QRCodeDetectorインスタンス生成
    qrd = cv2.QRCodeDetector()

    # QRコードデコード
    retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(img_bgr)

    if retval:
        points = points.astype(np.int)

        for dec_inf, point in zip(decoded_info, points):
            if dec_inf == '':
                continue

            # QRコード座標取得
            x = point[0][0]
            y = point[0][1]

            # QRコードデータ
            print('dec:', dec_inf)
            img_bgr = cv2.putText(
                img_bgr,
                dec_inf,
                (x, y-6),
                font,
                .3,
                (0, 0, 255),
                1,
                cv2.LINE_AA
                )

            # バウンディングボックス
            img_bgr = cv2.polylines(img_bgr,
                                    [point],
                                    True,
                                    (0, 255, 0),
                                    1,
                                    cv2.LINE_AA
                                    )

    cv2.imshow('image', img_bgr)
    cv2.waitKey(0)


if __name__ == '__main__':

    create_qrcode('Arctic.png', 'Arctic')   # 北極
    create_qrcode('Great_Barrier_Reef.png', 'Great_Barrier_Reef')

    # im1 = cv2.imread(FILE_PNG_A)
    # im2 = cv2.imread(FILE_PNG_B)

    # im_h = cv2.hconcat([im1, im2])
    # cv2.imwrite(FILE_PNG_AB, im_h)

    # img_BGR = cv2.imread(FILE_PNG_AB, cv2.IMREAD_COLOR)
    # qrdec_cv2(img_BGR)
