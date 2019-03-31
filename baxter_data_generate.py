


import os, pickle, cv2, IPython


if __name__ == '__main__':

    data_simu_x = []
    data_simu_v = []
    data_real_x = []

    for i in range(350):
        if os.path.exists('datasets/baxter/data_2colli/data_simu_' + str(i) + '.pkl'):
            data_load = open('datasets/baxter/data_2colli/data_simu_' + str(i) + '.pkl', 'rb')
            data_simu_q = pickle.load(data_load)
            count = 0
            for data in data_simu_q:
                if count >= 60:
                    break
                count += 1
                if i < 100 and count % 2 == 1:
                    continue
                # IPython.embed()
                cv2.imwrite('datasets/baxter/trainA/A_' + str(i) + '_' + str(count) + '.jpg', data[0].squeeze())

    for i in range(350):
        if os.path.exists('datasets/baxter/data_2colli/data_real_' + str(i) + '.pkl'):
            data_load = open('datasets/baxter/data_2colli/data_real_' + str(i) + '.pkl', 'rb')
            data_real_q = pickle.load(data_load)
            count = 0
            for data in data_real_q:
                if count >= 60:
                    break
                count += 1
                if i < 100 and count % 2 == 1:
                    continue
                cv2.imwrite('datasets/baxter/trainB/B_' + str(i) + '_' + str(count) + '.jpg', data[0].squeeze())