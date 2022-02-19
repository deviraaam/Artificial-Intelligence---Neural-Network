#include<stdio.h>
#include<math.h>
#include<stdlib.h>

main(void)
{
    int i,j,k,l,m,n,o,epoch,p,q,r,z;
    float w[15][15], h[15], sig[15],C, wh[15],sigc[15],error,miu,dc, dwh[15],dh[15],dwi[15][15],perf,MSE,SSE,I[300][300], target[300];

    miu = 0.1;

    for(i=0;i<=13; i++)
    {
        for(j=1; j<=13; j++)
        {
            w[i][j] = rand()%100/99.1938129;
            //printf("w[%d][%d] = %f\n\n",i,j,w[i][j]);
        }
    }

    for(i=0; i<=13; i++)
    {
        wh[i] = rand()%100/99.21372819372;
        //printf("wh[%d] = %f\n",i,wh[i]);
    }

    freopen("input.txt","r",stdin);
    scanf("%d", &z);
    for( int r= 1; r <= z; r++)
    {
        for(j=1; j<=13; j++)
        {
            scanf("%f", &I[j][r]);
            //printf("I[%d][%d] = %f\n",j,r,I[j][r]);
        }
        scanf("%f",&target[r]);
        //printf("Target[%d] = %f\n",r,target[r]);
    }

    for(epoch=1; epoch<= 1000; epoch++)
    {
        printf("EPOCH = %d\n",epoch);
        //printf("FEED FORWARD\n");

        for(i=1; i<=z; i++)
        {
           for(j=1; j<=13; j++)
           {
               h[j] = 1*w[0][j] + I[1][i]*w[1][j] + I[2][i]*w[2][j] + I[3][i]*w[3][j] + I[4][i]*w[4][j] + I[5][i]*w[5][j]
                + I[6][i]*w[6][j] + I[7][i]*w[7][j] + I[8][i]*w[8][j] + I[9][i]*w[9][j] + I[10][i]*w[10][j] + I[11][i]*w[11][j] + I[12][i]*w[12][j] + I[13][i]*w[13][j];
               sig[j] = 1/(1+exp(-h[j]));
               h[j] = sig[j];
               //printf("%d h[%d] = %f\n",i, j, h[j]);
           }

           C = 1*wh[0] + h[1]*wh[1] + h[2]*wh[2] + h[3]*wh[3] + h[4]*wh[4] + h[5]*wh[5] + h[6]*wh[6] + h[7]*wh[7] + h[8]*wh[8] + h[9]*wh[9] + h[10]*wh[10] + h[11]*wh[11]
            + h[12]*wh[12] + h[13]*wh[13];
           sigc[i] =1/(1+exp(-C));
           //printf("C = %f\nsigc = %f\n",C,sigc[i]);

           //printf("target[%d] = %d\n",i,target[i]);
           error = target[i] - sigc[i];
           //printf("Error = %f\n", error);

           //printf("\nBACK PROPAGASI\n");
           dc = sigc[i]*(1-sigc[i])*(target[i]-sigc[i]);
            //printf("dc = %f\n",dc);

           dwh[0] = miu*1*dc;
           wh[0] = wh[0] + dwh[0];
           //printf("dwh[0] = %f\nwh[0] = %f\n",dwh[0],wh[0]);
           for(k=1; k<=13; k++)
           {
               dwh[k] = miu*h[k]*dc;
               wh[k] = wh[k] + dwh[k];
               //printf("dwh[%d] = %f\nwh[%d] = %f\n",k, dwh[k], k, wh[k]);
           }

           for(l=1; l<=13; l++)
           {
               dh[l] = h[l]*(1-h[l])*wh[l]*dc;
           // printf("dh[%d] = %f\n",l,dh[l]);
           }

            for(p=1; p<=13; p++)
            {
                dwi[0][p] = miu*1*dh[p];
                w[0][p] = w[0][p] + dwi[0][p];
                //printf("w[0][%d] = %f\n",p,dwi[0][p]);
            }
           for(m=1; m<=13; m++)
           {
               for(n=1; n<=13; n++)
               {
                   dwi[m][n] = miu*I[n][i]*dh[n];
                   w[m][n] = w[m][n] + dwi[m][n];
                   //printf("dwi[%d][%d] = %f\n wi[%d][%d] = %f\n",m,n, dwi[m][n],m,n,w[m][n]);
               }
           }
           //printf("\n============== GANTI INPUT ===============\n");
        }

        for(o=1; o<=270; o++)
        {
            if(sigc[o]>=0.8)
            {
                sigc[0]=1;
            }
            else if(sigc[o]<=0.2)
            {
                sigc[o] =0;
            }
        }

        SSE = 0;
        for(q=1;q<=z; q++)
        {
            SSE = SSE+pow((target[q]-sigc[q]),2);
        }
       MSE=SSE/z;
       printf("MSE = %f\n",MSE);
    }
}
