# 2nm节点  High-NA 是必须吗？有没有可能，咱们都让Intel带跑偏了！

        
            [来自：
                半导体大佬的会议室](https://wx.zsxq.com/group/88888812815442)
        
        
            
                

![](images/39ac34f1b548792d9368.jpg)

                吴梓豪leslie
            
            2024年05月23日 16:23
        
        
            

![](images/97ae921e97a9dc429b43.png)

5月份媒体开始转发台积电在2nm不用High-NA的文章 , 除了台积电自己发布了部分消息 , 许多海外的专业媒体也跟踪报导 , 内地媒体复制翻译转发 , 但这些无一例外都没说到根子上 , 也就是没从技术理论的基础来 , 所以我们今天从最基础的理论来计算下 , 倒底需要还是不需要 ?

 

台积电会在2nm用High-NA EUV吗？ 答案是不会，很大可能连下一代的A14都不会用！

 

这个问题大家可能被Intel最近交付5000系列也就是High-NA EUV给带偏了，事实上未来半导体发展到什么节点需要NA达到0.55的High-NA呢？

 

首先咱们来看一下half pitch这是行业习惯用语，跟光刻最高分辨率是等意词

 

也就是half pitch = k1*λ0／n* sinθ=R 。 low-NA EUV 波长13.5nm , NA:0.33 , k1的话在传统OAI或PSM增益技术跟OPC的SMO叠加使用可以从0.28降低至0.25 , 也就是能获得10.2nm的图形 , high-NA则是6nm . SAMP的多曝手段可以将k1直接降一半到0.125 , low-NA透过多曝可以将图形特征尺寸降到5nm甚至更低 , 但这一切都是理论值

 

目前各家的5nm，不论intel、TSMC、SS的MMP（最小金属周距）都是28nm, 台积电的第一代是30nm , 3nm降到23nm , 2nm在20nm , 这些数字除1/2就是咱们说的half-MP（M0/M1半周距） , 根据IMEC路线，A14(1.4nm)以下A10~A3节点的MMP可能都会维持在16nm不变 , 主要靠FSFET、CFET结构来增加晶体管数量 , 也就是half-MP在8nm , 如此的话MMP：20nm的N2应该是low-NA的最后一代 , 因为上面我们算出了low-NA的half pitch是10nm 两者一致 .

 

我手边没有A14的MMP 就算是18nm好了 , half-pitch是9nm，已经低于10nm , 因为多曝以外的RET增益技术都用上了 , 所以只剩下多曝可以降低k1 , IMEC跟Mentor合作开发的SALELE自然能用上 , 也就是说A14 的half-pitch虽然低于10nm但low-NA加上相对简单的多曝可以搞定 .

 

其实最上面的算式我们已经算出low-NA透过SAMP做到5nm的MMP是可以做到的 , 但实际上做不到 , 量子遂穿的漏电是大问题 , 除非材料有新的突破 , 这里面也牵涉CCP , cell高度 , fin pitch等等关键尺寸的设计 , 各家不一

 

这样讨论下来 , 目前光刻机技术是有冗余 , 最终还是成本如何平衡的问题 , 这样算下来 A14不用high-NA技术以及理论基础上完全没问题 , 成本也是可控并合理的 , 其实从什么节点要使用high-NA这一点来观察 , TSMC跟Intel的制程水平是有一定差距的。

        
        

![](images/97ae921e97a9dc429b43.png)

5月份媒体开始转发台积电在2nm不用High-NA的文章 , 除了台积电自己发布了部分消息 , 许多海外的专业媒体也跟踪报导 , 内地媒体复制翻译转发 , 但这些无一例外都没说到根子上 , 也就是没从技术理论的基础来 , 所以我们今天从最基础的理论来计算下 , 倒底需要还是不需要 ?

 

台积电会在2nm用High-NA EUV吗？ 答案是不会，很大可能连下一代的A14都不会用！

 

这个问题大家可能被Intel最近交付5000系列也就是High-NA EUV给带偏了，事实上未来半导体发展到什么节点需要NA达到0.55的High-NA呢？

 

首先咱们来看一下half pitch这是行业习惯用语，跟光刻最高分辨率是等意词

 

也就是half pitch = k1*λ0／n* sinθ=R 。 low-NA EUV 波长13.5nm , NA:0.33 , k1的话在传统OAI或PSM增益技术跟OPC的SMO叠加使用可以从0.28降低至0.25 , 也就是能获得10.2nm的图形 , high-NA则是6nm . SAMP的多曝手段可以将k1直接降一半到0.125 , low-NA透过多曝可以将图形特征尺寸降到5nm甚至更低 , 但这一切都是理论值

 

目前各家的5nm，不论intel、TSMC、SS的MMP（最小金属周距）都是28nm, 台积电的第一代是30nm , 3nm降到23nm , 2nm在20nm , 这些数字除1/2就是咱们说的half-MP（M0/M1半周距） , 根据IMEC路线，A14(1.4nm)以下A10~A3节点的MMP可能都会维持在16nm不变 , 主要靠FSFET、CFET结构来增加晶体管数量 , 也就是half-MP在8nm , 如此的话MMP：20nm的N2应该是low-NA的最后一代 , 因为上面我们算出了low-NA的half pitch是10nm 两者一致 .

 

我手边没有A14的MMP 就算是18nm好了 , half-pitch是9nm，已经低于10nm , 因为多曝以外的RET增益技术都用上了 , 所以只剩下多曝可以降低k1 , IMEC跟Mentor合作开发的SALELE自然能用上 , 也就是说A14 的half-pitch虽然低于10nm但low-NA加上相对简单的多曝可以搞定 .

 

其实最上面的算式我们已经算出low-NA透过SAMP做到5nm的MMP是可以做到的 , 但实际上做不到 , 量子遂穿的漏电是大问题 , 除非材料有新的突破 , 这里面也牵涉CCP , cell高度 , fin pitch等等关键尺寸的设计 , 各家不一

 

这样讨论下来 , 目前光刻机技术是有冗余 , 最终还是成本如何平衡的问题 , 这样算下来 A14不用high-NA技术以及理论基础上完全没问题 , 成本也是可控并合理的 , 其实从什么节点要使用high-NA这一点来观察 , TSMC跟Intel的制程水平是有一定差距的。

        

![](images/97ae921e97a9dc429b43.png)

5月份媒体开始转发台积电在2nm不用High-NA的文章 , 除了台积电自己发布了部分消息 , 许多海外的专业媒体也跟踪报导 , 内地媒体复制翻译转发 , 但这些无一例外都没说到根子上 , 也就是没从技术理论的基础来 , 所以我们今天从最基础的理论来计算下 , 倒底需要还是不需要 ?

 

台积电会在2nm用High-NA EUV吗？ 答案是不会，很大可能连下一代的A14都不会用！

 

这个问题大家可能被Intel最近交付5000系列也就是High-NA EUV给带偏了，事实上未来半导体发展到什么节点需要NA达到0.55的High-NA呢？

 

首先咱们来看一下half pitch这是行业习惯用语，跟光刻最高分辨率是等意词

 

也就是half pitch = k1*λ0／n* sinθ=R 。 low-NA EUV 波长13.5nm , NA:0.33 , k1的话在传统OAI或PSM增益技术跟OPC的SMO叠加使用可以从0.28降低至0.25 , 也就是能获得10.2nm的图形 , high-NA则是6nm . SAMP的多曝手段可以将k1直接降一半到0.125 , low-NA透过多曝可以将图形特征尺寸降到5nm甚至更低 , 但这一切都是理论值

 

目前各家的5nm，不论intel、TSMC、SS的MMP（最小金属周距）都是28nm, 台积电的第一代是30nm , 3nm降到23nm , 2nm在20nm , 这些数字除1/2就是咱们说的half-MP（M0/M1半周距） , 根据IMEC路线，A14(1.4nm)以下A10~A3节点的MMP可能都会维持在16nm不变 , 主要靠FSFET、CFET结构来增加晶体管数量 , 也就是half-MP在8nm , 如此的话MMP：20nm的N2应该是low-NA的最后一代 , 因为上面我们算出了low-NA的half pitch是10nm 两者一致 .

 

我手边没有A14的MMP 就算是18nm好了 , half-pitch是9nm，已经低于10nm , 因为多曝以外的RET增益技术都用上了 , 所以只剩下多曝可以降低k1 , IMEC跟Mentor合作开发的SALELE自然能用上 , 也就是说A14 的half-pitch虽然低于10nm但low-NA加上相对简单的多曝可以搞定 .

 

其实最上面的算式我们已经算出low-NA透过SAMP做到5nm的MMP是可以做到的 , 但实际上做不到 , 量子遂穿的漏电是大问题 , 除非材料有新的突破 , 这里面也牵涉CCP , cell高度 , fin pitch等等关键尺寸的设计 , 各家不一

 

这样讨论下来 , 目前光刻机技术是有冗余 , 最终还是成本如何平衡的问题 , 这样算下来 A14不用high-NA技术以及理论基础上完全没问题 , 成本也是可控并合理的 , 其实从什么节点要使用high-NA这一点来观察 , TSMC跟Intel的制程水平是有一定差距的。

        
                
                

![](/assets_dweb/logo@1x.png)

                知识星球
                
        
        
            
            扫码加入星球
            查看更多优质内容
        
        https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88888812815442

---

Source: https://articles.zsxq.com/id_0e7znxfwww2v.html

Linked from topic_id: 5122585484555454
